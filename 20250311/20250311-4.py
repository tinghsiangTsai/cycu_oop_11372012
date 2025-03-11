# 創建一個包含星期一到星期日的列表
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
# 創建一個包含一月到十二月的列表
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

# 獲取使用者輸入的月份
month = int(input("Enter the month (1-12): "))

# 輸出對應的英文月份名稱
if 1 <= month <= 12:
    print(months[month - 1])
else:
    print("Invalid month. Please enter a number between 1 and 12.")
