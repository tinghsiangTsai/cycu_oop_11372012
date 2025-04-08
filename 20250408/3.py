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

#列出C:\Users\User\Desktop\cycu_oop_11372012\20250408\stops_of_route.html中所有auto-list-stationlist-place的資料並列出
from bs4 import BeautifulSoup
import os

# 讀取 HTML 檔案
with open(file_path, "r", encoding="utf-8") as file:
    html_content = file.read()
    soup = BeautifulSoup(html_content, "html.parser")
    # 找到所有 class 為 auto-list-stationlist-place 的元素
    elements = soup.find_all(class_="auto-list-stationlist-place")
    # 列出所有元素的內容
    for element in elements:
        print(element.get_text(strip=True))

#列出C:\Users\User\Desktop\cycu_oop_11372012\20250408\stops_of_route.html中所有auto-list-stationlist-number的資料並列出
from bs4 import BeautifulSoup
import os

# 讀取 HTML 檔案
with open(file_path, "r", encoding="utf-8") as file:
    html_content = file.read()
    soup = BeautifulSoup(html_content, "html.parser")
    # 找到所有 class 為 auto-list-stationlist-number 的元素
    elements = soup.find_all(class_="auto-list-stationlist-number")
    # 列出所有元素的內容
    for element in elements:
        print(element.get_text(strip=True))

#列出C:\Users\User\Desktop\cycu_oop_11372012\20250408\stops_of_route.html中所有auto-list-stationlist-position auto-list-stationlist-position-time的資料並列出
from bs4 import BeautifulSoup
import os

# 讀取 HTML 檔案
with open(file_path, "r", encoding="utf-8") as file:
    html_content = file.read()
    soup = BeautifulSoup(html_content, "html.parser")
    # 找到所有 class 為 auto-list-stationlist-position auto-list-stationlist-position-time 的元素
    elements = soup.find_all(class_="auto-list-stationlist-position auto-list-stationlist-position-time")
    # 列出所有元素的內容
    for element in elements:
        print(element.get_text(strip=True))

#列出C:\Users\User\Desktop\cycu_oop_11372012\20250408\stops_of_route.html中所有value的資料並列出
from bs4 import BeautifulSoup
import os

# 讀取 HTML 檔案
with open(file_path, "r", encoding="utf-8") as file:
    html_content = file.read()
    soup = BeautifulSoup(html_content, "html.parser")
    # 找到所有 class 為 value 的元素
    elements = soup.find_all(class_="value")
    # 列出所有元素的內容
    for element in elements:
        print(element.get_text(strip=True))

#列出C:\Users\User\Desktop\cycu_oop_11372012\20250408\stops_of_route.html中所有value的資料並列出
from bs4 import BeautifulSoup
import os

# 讀取 HTML 檔案
with open(file_path, "r", encoding="utf-8") as file:
    html_content = file.read()
    soup = BeautifulSoup(html_content, "html.parser")
    # 找到所有 class 為 value 的元素
    elements = soup.find_all(class_="value")
    # 列出所有元素的內容
    for element in elements:
        print(element.get_text(strip=True))
    
    