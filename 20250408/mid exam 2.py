from datetime import datetime, timezone
import sys
import io

# 防止中文亂碼
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


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


def time_info(input_time_str: str):
    try:
        dt = datetime.strptime(input_time_str, '%Y-%m-%d %H:%M')
        dt = dt.replace(tzinfo=timezone.utc)

        weekday = dt.strftime('%A')
        input_jd = datetime_to_julian_date(dt)

        now = datetime.now(timezone.utc)
        now_jd = datetime_to_julian_date(now)

        diff_days = now_jd - input_jd

        print(f"\n輸入時間：{input_time_str}")
        print(f"星期幾：{weekday}")
        print(f"輸入時間的 Julian Date：{input_jd:.5f}")
        print(f"目前時間的 Julian Date：{now_jd:.5f}")
        print(f"相隔的太陽日（Julian days）：{diff_days:.5f}\n")

    except ValueError:
        print("❌ 錯誤：請輸入格式為 YYYY-MM-DD HH:MM 的時間字串")


# ✅ 加入互動輸入
if __name__ == "__main__":
    user_input = input("請輸入時間（格式為 YYYY-MM-DD HH:MM）：")
    time_info(user_input)
