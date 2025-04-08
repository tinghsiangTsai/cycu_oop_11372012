import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import lognorm

def plot_lognorm_cdf(mu, sigma, x_range=(0.01, 10), num_points=1000, output_file="lognorm_cdf.jpg"):
    """
    繪製對數常態分布的累積分布函數（CDF）圖，並儲存為 JPG 檔案。

    參數:
    - mu: 對數常態分布的 μ（對數平均）
    - sigma: 對數常態分布的 σ（對數標準差）
    - x_range: x 軸的範圍 (起點, 終點)
    - num_points: 圖上點的數量
    - output_file: 輸出檔案名稱（含副檔名 .jpg）
    """
    # 產生 x 值
    x = np.linspace(x_range[0], x_range[1], num_points)

    # 計算 lognormal 的 CDF
    cdf = lognorm.cdf(x, s=sigma, scale=np.exp(mu))  # scipy 的 scale = exp(mu)

    # 繪圖
    plt.figure(figsize=(8, 5))
    plt.plot(x, cdf, label=f'μ={mu}, σ={sigma}', color='blue')
    plt.title("Log-Normal Cumulative Distribution Function")
    plt.xlabel("x")
    plt.ylabel("CDF")
    plt.grid(True)
    plt.legend()
    
    # 儲存為 JPG
    plt.savefig(output_file, format='jpg', dpi=300)
    plt.close()
    print(f"Image saved as:{output_file}")
if __name__ == "__main__":
    plot_lognorm_cdf(mu=1.5, sigma=0.4)
import os

if __name__ == "__main__":
    filename = "lognorm_cdf.jpg"
    plot_lognorm_cdf(mu=1.5, sigma=0.4, output_file=filename)
    os.startfile(filename)  # 在 Windows 系統中自動開啟檔案
