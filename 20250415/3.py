# %% 公車站點爬蟲（修正亂碼：使用 utf-8-sig 編碼）
import csv
import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

def scrape_bus_stops(route_id: str, output_file: str):
    # 建立目標網址
    target_url = f"https://ebus.gov.taipei/Route/StopsOfRoute?routeid={route_id}"
    print(f"🔗 正在爬取：{target_url}")

    # 設定瀏覽器為無頭模式（不開啟視窗）
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920x1080")

    # 啟動 Chrome 瀏覽器
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(target_url)
    time.sleep(3)  # 等待 JavaScript 載入完成
    html = driver.page_source
    driver.quit()

    # 使用 BeautifulSoup 解析 HTML
    soup = BeautifulSoup(html, "html.parser")
    stops = soup.find_all("a", class_="auto-list-link auto-list-stationlist-link")

    # 確保資料夾存在
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    # 儲存為 UTF-8 with BOM，讓 Excel 不會出現亂碼
    with open(output_file, mode="w", encoding="utf-8-sig", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["arrival_info", "stop_number", "stop_name", "stop_id", "latitude", "longitude"])

        for stop in stops:
            span = stop.find("span", class_="auto-list auto-list-stationlist")
            if span:
                arrival = span.find("span", class_="auto-list-stationlist-position auto-list-stationlist-position-time")
                number = span.find("span", class_="auto-list-stationlist-number")
                name = span.find("span", class_="auto-list-stationlist-place")
                stop_id = span.find("input", id="item_UniStopId")
                lat = span.find("input", id="item_Latitude")
                lon = span.find("input", id="item_Longitude")

                row = [
                    arrival.text.strip() if arrival else "無資料",
                    number.text.strip() if number else "",
                    name.text.strip() if name else "",
                    stop_id["value"] if stop_id else "",
                    lat["value"] if lat else "",
                    lon["value"] if lon else ""
                ]
                writer.writerow(row)

    print(f"✅ 完成爬取！資料已儲存至：\n📄 {os.path.abspath(output_file)}")

# === 主程式執行區塊 ===
if __name__ == "__main__":
    route_input = input("請輸入公車代碼（預設：0100000A00）：").strip() or "0100000A00"

    # ✅ 設定明確儲存路徑
    output_path = "C:/Users/鼎翔/Desktop/cycu_oop_11372012/20250415/bus_stops.csv"

    # ✅ 執行爬蟲
    scrape_bus_stops(route_id=route_input, output_file=output_path)
