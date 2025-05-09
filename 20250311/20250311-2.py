import pandas as pd

# 讀取 Excel 檔案
file_path = '311.xlsx'
df = pd.read_excel(file_path)

# 假設 Excel 檔案有兩個欄位 'x' 和 'y'
df['sum'] = df['x'] + df['y']

# 列印結果
print(df['sum'])