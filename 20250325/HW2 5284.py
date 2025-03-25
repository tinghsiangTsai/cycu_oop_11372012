import requests
import json
from datetime import datetime, timedelta

# PTX API的URL
api_url = "https://ptx.transportdata.tw/MOTC/v2/Bus/EstimatedTimeOfArrival/City/Taipei/忠孝幹線?&$format=JSON"

# 輸入的站名
input_stop_name = "正義重新路口"

# 發送GET請求
response = requests.get(api_url)

# 檢查請求是否成功
if response.status_code == 200:
    data = response.json()
    # 遍歷所有預估到站時間的資料
    for item in data:
        stop_name = item.get("StopName", {}).get("Zh_tw", "")
        route_direction = item.get("Direction", 0)
        estimate_time = item.get("EstimateTime", None)
        stop_status = item.get("StopStatus", None)
        # 檢查站名是否匹配且方向為去程（Direction為0表示去程）
        if stop_name == input_stop_name and route_direction == 0:
            if stop_status == 0 and estimate_time is not None:
                # 計算還有多少分鐘到站
                minutes = estimate_time // 60
                print(f"公車預計還有 {minutes} 分鐘到達 {input_stop_name}。")
            elif stop_status == 1:
                print(f"{input_stop_name} 站目前不停靠。")
            elif stop_status == 2:
                print(f"{input_stop_name} 站已過站，請等待下一班公車。")
            elif stop_status == 3:
                print(f"目前沒有即將到達 {input_stop_name} 的公車。")
            elif stop_status == 4:
                print(f"{input_stop_name} 站尚未發車。")
else:
    print(f"無法取得資料，HTTP狀態碼：{response.status_code}")
