from datetime import datetime, timezone
import sys
import io

# 防止中文亂碼（VS Code / Windows 命令列常見問題）
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# ✅ 轉換 datetime → Julian Date
def datetime_to_julian_date(dt: datetime) -> float:
    year = dt.year
    month = dt.month
    day = dt.day + dt.hour / 24 + dt.minute / 1440 + dt.second / 86400

    if month <= 2:
        year -= 1
        month += 12

    A = year // 100
    B = 2 - A + A // 4

    jd = int(365.25 * (year + 4716)) + int(30.6001 * (month + 1)) + day + B - 1524.5
    return jd

# ✅ 處理主功能：星期幾 + 太陽日
def time_info(input_time_str: str):
    try:
        # 自動判斷是否有輸入秒數
        time_format = '%Y-%m-%d %H:%M:%S' if len(input_time_str.strip()) == 19 else '%Y-%m-%d %H:%M'
        dt = datetime.strptime(input_time_str, time_format)
        dt = dt.replace(tzinfo=timezone.utc)

        weekday = dt.strftime('%A')  # 英文星期幾
        input_jd = datetime_to_julian_date(dt)

        now = datetime.now(timezone.utc)
        now_jd = datetime_to_julian_date(now)

        diff_days = now_jd - input_jd

        print(f"\n🕒 輸入時間：{input_time_str}")
        print(f"📅 星期幾：{weekday}")
        print(f"🪐 輸入時間的 Julian Date：{input_jd:.5f}")
        print(f"🌍 現在時間的 Julian Date：{now_jd:.5f}")
        print(f"⏳ 相隔的太陽日（Julian Days）：{diff_days:.5f}\n")

    except ValueError:
        print("❌ 錯誤：請輸入格式為 'YYYY-MM-DD HH:MM' 或 'YYYY-MM-DD HH:MM:SS' 的時間")

# ✅ 執行進入點
if __name__ == "__main__":
    user_input = input("請輸入時間（格式為 YYYY-MM-DD HH:MM 或 YYYY-MM-DD HH:MM:SS）：")
    time_info(user_input)
