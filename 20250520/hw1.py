import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

# 取得目前程式所在的資料夾路徑
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "midterm_scores.csv")

# 讀取 CSV 檔案
df = pd.read_csv(csv_path)

# 指定科目順序（國文起頭）
subjects = ['Chinese', 'English', 'Math', 'History', 'Geography', 'Physics', 'Chemistry']

# 對應彩虹顏色
rainbow_colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

# 分數分組區間（0~10, 10~20, ..., 90~100）
bins = list(range(0, 101, 10))
labels = [f"{i}-{i+10}" for i in bins[:-1]]

# 建立統計用 DataFrame
hist_df = pd.DataFrame(index=labels, columns=subjects).fillna(0)

# 統計每科在每個分數區間的人數
for subject in subjects:
    counts = pd.cut(df[subject], bins=bins, right=False, labels=labels).value_counts().sort_index()
    hist_df[subject] = counts

# 畫圖（每科各自一組 bar）
x = np.arange(len(labels))
width = 0.1
plt.figure(figsize=(18, 8))

for i, (subject, color) in enumerate(zip(subjects, rainbow_colors)):
    plt.bar(x + i * width, hist_df[subject], width=width, label=subject, color=color)

# 標籤與圖例設定
plt.xticks(x + width * (len(subjects) / 2 - 0.5), labels, rotation=45)
plt.xlabel("Score Range")
plt.ylabel("Number of Students")
plt.title("Score Distribution by Subject (Colored by Rainbow)")
plt.legend()
plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.show()
