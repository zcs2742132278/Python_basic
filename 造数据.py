import numpy as np
import pandas as pd

# ---------------------- 1. 构造线性数据 ----------------------
np.random.seed(42)  # 固定随机种子，每次运行数据一样
x = np.linspace(0, 100, 300)  # 生成 0~100 之间 300 个均匀点

# 线性关系：y = 2.5 * x + 10 + 噪声
true_w = 2.5   # 真实权重
true_b = 10    # 真实偏置
noise = np.random.normal(0, 15, size=len(x))  # 高斯噪声
y = true_w * x + true_b + noise

# ---------------------- 2. 保存为 CSV ----------------------
df = pd.DataFrame({
    "x": x,
    "y": y
})
df.to_csv("./datas/linear_data.csv", index=False, encoding="utf-8")

print("✅ CSV 文件已生成：linear_data.csv")
print("\n前5行数据：")
print(df.head())