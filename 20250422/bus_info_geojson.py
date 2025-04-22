import geopandas as gpd
import matplotlib.pyplot as plt
import folium
import os

# === 讀取 GeoJSON 檔案 === #
file_path = r"C:\Users\User\Desktop\cycu_oop_11372012\20250422\bus_stops.geojson"
gdf = gpd.read_file(file_path)

# === 檢查資料內容（可選）=== #
print(gdf.head())

# === 畫出站點圖（使用 Matplotlib）=== #
plt.figure(figsize=(10, 10))
gdf.plot(marker='o', color='blue', markersize=5)
plt.title("Bus Stops Location Map")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.grid(True)
plt.axis("equal")

# === 儲存成 PNG 檔案 === #
output_png = os.path.join(os.path.dirname(file_path), "bus_stops_map.png")
plt.savefig(output_png, dpi=300)
plt.close()
print(f"PNG 檔儲存完成：{output_png}")

# === 使用 Folium 製作互動地圖（另存為 HTML）=== #
# 預設中心點設定為資料的平均值
center = [gdf.geometry.y.mean(), gdf.geometry.x.mean()]
m = folium.Map(location=center, zoom_start=13)

# 加入每個站點的標記
for _, row in gdf.iterrows():
    folium.CircleMarker(
        location=[row.geometry.y, row.geometry.x],
        radius=3,
        color='blue',
        fill=True,
        fill_opacity=0.7,
        popup=row.get('name', 'Bus Stop')  # 若有 name 欄位則顯示
    ).add_to(m)

# 儲存 HTML 互動地圖
output_html = os.path.join(os.path.dirname(file_path), "bus_stops_map.html")
m.save(output_html)
print(f"互動地圖 HTML 檔儲存完成：{output_html}")
