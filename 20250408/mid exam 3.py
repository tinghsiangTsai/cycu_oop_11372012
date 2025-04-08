from playwright.sync_api import sync_playwright

# 目標 URL
url = "https://ebus.gov.taipei/Route/StopsOfRoute?routeid=0100000A00"

# 使用 Playwright 渲染 HTML
with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)  # 啟動無頭瀏覽器
    context = browser.new_context()
    page = context.new_page()
    page.goto(url)  # 瀏覽到目標 URL
    rendered_html = page.content()  # 獲取渲染後的 HTML
    browser.close()

# 將 HTML 內容儲存到指定檔案
file_path = r"C:\\Users\\User\\Desktop\\cycu_oop_11372012\\20250408\\stops_of_route.html"
with open(file_path, "w", encoding="utf-8") as file:
    file.write(rendered_html)

print(f"HTML 已成功儲存到 {file_path}")

from bs4 import BeautifulSoup

# HTML 檔案路徑
file_path = r"C:\\Users\\User\\Desktop\\cycu_oop_11372012\\20250408\\stops_of_route.html"

# 讀取 HTML 檔案
with open(file_path, "r", encoding="utf-8") as file:
    html_content = file.read()

# 使用 BeautifulSoup 解析 HTML
soup = BeautifulSoup(html_content, "html.parser")

# 找到所有站點資料
bus_stops = []
stop_elements = soup.find_all("a", class_="auto-list-link auto-list-stationlist-link")

for stop in stop_elements:
    stop_data = stop.find("span", class_="auto-list auto-list-stationlist")
    if stop_data:
        # 提取資料
        arrival_info = stop_data.find("span", class_="auto-list-stationlist-position auto-list-stationlist-position-time")
        stop_number = stop_data.find("span", class_="auto-list-stationlist-number").text.strip()
        stop_name = stop_data.find("span", class_="auto-list-stationlist-place").text.strip()
        stop_id = stop_data.find("input", {"id": "item_UniStopId"})["value"]
        latitude = stop_data.find("input", {"id": "item_Latitude"})["value"]
        longitude = stop_data.find("input", {"id": "item_Longitude"})["value"]

        # 將資料加入列表
        bus_stops.append({
            "arrival_info": arrival_info.text.strip() if arrival_info else None,
            "stop_number": stop_number,
            "stop_name": stop_name,
            "stop_id": stop_id,
            "latitude": latitude,
            "longitude": longitude
        })

# 輸出結果
for stop in bus_stops:
    print(stop)