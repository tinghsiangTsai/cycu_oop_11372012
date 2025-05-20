import geopandas as gpd
import matplotlib.pyplot as plt

# GeoJSON 檔案位置（請依實際路徑修改）
geojson_path = r"C:\Users\User\Desktop\cycu_oop_11372012\20250520\northern_taiwan_filtered.geojson"

# 讀取 GeoJSON
gdf = gpd.read_file(geojson_path)

# 繪圖
plt.figure(figsize=(10, 10))
gdf.plot(edgecolor='black', color='lightskyblue')
plt.title("北北基桃行政區界圖", fontsize=16)
plt.axis("equal")
plt.tight_layout()
plt.show()
