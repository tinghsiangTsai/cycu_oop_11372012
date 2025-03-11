import pandas as pd
import matplotlib.pyplot as plt

# 讀取 Excel 檔案
file_path = '311.xlsx'
df = pd.read_excel(file_path)

# 假設 Excel 檔案有兩個欄位 'x' 和 'y'
df['sum'] = df['x'] + df['y']

# 列印結果
print(df['sum'])

# 繪製散佈圖
plt.scatter(df['x'], df['y'])
plt.xlabel('x')
plt.ylabel('y')
plt.title('Scatter plot of x and y')
plt.show()
