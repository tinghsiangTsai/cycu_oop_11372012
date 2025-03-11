import lunarcalendar
from lunarcalendar.converter import Converter
from lunarcalendar import Lunar, Solar

def get_chinese_zodiac(year):
    zodiacs = ["鼠", "牛", "虎", "兔", "龍", "蛇", "馬", "羊", "猴", "雞", "狗", "豬"]
    return zodiacs[(year - 4) % 12]

def main():
    year = int(input("請輸入西元年: "))
    month = int(input("請輸入月: "))
    day = int(input("請輸入日: "))

    solar_date = Solar(year, month, day)
    lunar_date = Converter.Solar2Lunar(solar_date)

    chinese_zodiac = get_chinese_zodiac(lunar_date.year)
    print(f"農曆日期: {lunar_date}")
    print(f"生肖: {chinese_zodiac}")

if __name__ == "__main__":
    main()