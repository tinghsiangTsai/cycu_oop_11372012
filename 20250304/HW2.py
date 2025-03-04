def gcd(a, b):
    # 基本情況：當 b 為 0 時，a 就是最大公因數
    if b == 0:
        return a
    # 遞迴步驟：將 b 和 a % b 作為參數傳遞給下一層遞迴
    return gcd(b, a % b)
print(gcd(11, 121))  
print(gcd(7, 49))  
