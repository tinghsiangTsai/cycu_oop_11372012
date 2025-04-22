import csv
import os
import time
import urllib.parse
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import folium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from shapely.geometry import Point

def scrape_bus_stops(route_id: str, output_csv: str, output_geojson: str):
    # 中文 route id 編碼
    encoded_route_id = urllib.parse.quote(route_id, safe="")

    # 建立網址
    url = f"https://ebus.gov.taipei/Route/StopsOfRoute?routeid={encoded_route_id}"
    print(f"\n🔗 正在爬取：{url}")

    # 設定無頭 Chrome
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920x1080")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    time.sleep(3)  # 等待 JS 載入
    html = driver.page_source
    driver.quit()

    soup = BeautifulSoup(html, "html.parser")
    stops = soup.find_all("a", class_="auto-list-link auto-list-stationlist-link")

    if not stops:
        print("⚠️ 無法取得站點資訊，請確認輸入的公車代碼是否正確。")
        return

    data = []
    for stop in stops:
        span = stop.find("span", class_="auto-list auto-list-stationlist")
        if span:
            arrival = (
                span.find("span", class_="auto-list-stationlist-position auto-list-stationlist-position-time") or
                span.find("span", class_="auto-list-stationlist-position auto-list-stationlist-position-now") or
                span.find("span", class_="auto-list-stationlist-position auto-list-stationlist-position-none")
            )
            number = span.find("span", class_="auto-list-stationlist-number")
            name = span.find("span", class_="auto-list-stationlist-place")
            stop_id = span.find("input", id="item_UniStopId")
            lat = span.find("input", id="item_Latitude")
            lon = span.find("input", id="item_Longitude")

            row = {
                "arrival_info": arrival.text.strip() if arrival else "無資料",
                "stop_number": number.text.strip() if number else "",
                "stop_name": name.text.strip() if name else "",
                "stop_id": stop_id["value"] if stop_id else "",
                "latitude": float(lat["value"]) if lat else None,
                "longitude": float(lon["value"]) if lon else None
            }
            data.append(row)

    # 儲存成 CSV
    df = pd.DataFrame(data)
    df.to_csv(output_csv, index=False, encoding="utf-8-sig")
    print(f"\n✅ CSV 儲存完成：{output_csv}")

    # 建立 GeoDataFrame 並存為 GeoJSON
    geometry = [Point(xy) for xy in zip(df["longitude"], df["latitude"])]
    gdf = gpd.GeoDataFrame(df, geometry=geometry, crs="EPSG:4326")
    gdf.to_file(output_geojson, driver='GeoJSON')
    print(f"✅ GeoJSON 儲存完成：{output_geojson}")

    return gdf  # 回傳供後續製圖使用

def visualize_stops(gdf: gpd.GeoDataFrame, output_dir: str):
    # Matplotlib 靜態圖
    plt.figure(figsize=(10, 10))
    gdf.plot(marker='o', color='blue', markersize=5)
    plt.title("Bus Stops Location Map")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.grid(True)
    plt.axis("equal")

    output_png = os.path.join(output_dir, "bus_stops_map.png")
    plt.savefig(output_png, dpi=300)
    plt.close()
    print(f"📷 PNG 地圖儲存完成：{output_png}")

    # Folium 互動地圖
    center = [gdf.geometry.y.mean(), gdf.geometry.x.mean()]
    m = folium.Map(location=center, zoom_start=13)

    for _, row in gdf.iterrows():
        folium.CircleMarker(
            location=[row.geometry.y, row.geometry.x],
            radius=3,
            color='blue',
            fill=True,
            fill_opacity=0.7,
            popup=row.get("stop_name", "Bus Stop")
        ).add_to(m)

    output_html = os.path.join(output_dir, "bus_stops_map.html")
    m.save(output_html)
    print(f"🌐 HTML 地圖儲存完成：{output_html}")

# 主程式
if __name__ == "__main__":
    route_input = input("請輸入公車代碼（可含中文，例如 1818中壢→臺北）：").strip() or "0100000A00"

    base_dir = os.path.join(os.path.expanduser("~"), "Desktop", "cycu_oop_11372012", "20250422")
    os.makedirs(base_dir, exist_ok=True)

    output_csv = os.path.join(base_dir, "bus_stops.csv")
    output_geojson = os.path.join(base_dir, "bus_stops.geojson")

    gdf = scrape_bus_stops(route_input, output_csv, output_geojson)
    if gdf is not None:
        visualize_stops(gdf, base_dir)
