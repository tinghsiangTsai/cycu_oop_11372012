from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import csv

def fetch_bus_route_info(route_id: str, output_csv: str = "bus_route_info.csv"):
    # 建立目標網址
    url = f"https://ebus.gov.taipei/Route/StopsOfRoute?routeid={route_id}"

    # 透過 Playwright 抓取網頁
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url)
        page.wait_for_timeout(3000)  # 等待動態資料載入
        html_content = page.content()
        browser.close()

    # 解析 HTML
    soup = BeautifulSoup(html_content, "html.parser")
    bus_stops = []

    stop_elements = soup.find_all("a", class_="auto-list-link auto-list-stationlist-link")
    for stop in stop_elements:
        stop_data = stop.find("span", class_="auto-list auto-list-stationlist")
        if stop_data:
            arrival_info = stop_data.find("span", class_="auto-list-stationlist-position auto-list-stationlist-position-time")
            stop_number = stop_data.find("span", class_="auto-list-stationlist-number")
            stop_name = stop_data.find("span", class_="auto-list-stationlist-place")
            stop_id_tag = stop_data.find("input", {"id": "item_UniStopId"})
            latitude_tag = stop_data.find("input", {"id": "item_Latitude"})
            longitude_tag = stop_data.find("input", {"id": "item_Longitude"})

            # 將資訊彙整進列表
            bus_stops.append([
                arrival_info.text.strip() if arrival_info else "",
                stop_number.text.strip() if stop_number else "",
                stop_name.text.strip() if stop_name else "",
                stop_id_tag["value"] if stop_id_tag else "",
                latitude_tag["value"] if latitude_tag else "",
                longitude_tag["value"] if longitude_tag else ""
            ])

    # 輸出 CSV
    with open(output_csv, "w", encoding="utf-8-sig", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["arrival_info", "stop_number", "stop_name", "stop_id", "latitude", "longitude"])
        writer.writerows(bus_stops)

    print(f"✅ 公車路線資料已儲存到：{output_csv}")

# ✅ 執行測試（可換其他路線代碼）
if __name__ == "__main__":
    fetch_bus_route_info("0100000A00", "bus_0100000A00.csv")