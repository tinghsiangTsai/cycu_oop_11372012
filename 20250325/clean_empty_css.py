from bs4 import BeautifulSoup

# 設定 HTML 檔案名稱
input_file = "[忠孝幹線(公車雙向轉乘優惠)]公車動態資訊.html"
output_file = "cleaned_bus_info.html"

# 讀取 HTML 檔案
with open(input_file, "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

# 尋找所有 <style> 標籤，並移除空白 CSS 區塊
for style_tag in soup.find_all("style"):
    if style_tag.string:
        lines = style_tag.string.split("}")
        cleaned = []
        for rule in lines:
            parts = rule.strip().split("{")
            if len(parts) == 2 and parts[1].strip() == "":
                continue  # 跳過空白區塊
            if len(parts) == 2:
                cleaned.append(f"{parts[0].strip()} {{{parts[1].strip()}}}")
        # 寫回 <style> 中
        style_tag.string = "}\n".join(cleaned) + "}"

# 儲存清理後的新 HTML
with open(output_file, "w", encoding="utf-8") as f:
    f.write(str(soup))

print(f"✅ 已移除空白 CSS 樣式，並儲存為：{output_file}")
