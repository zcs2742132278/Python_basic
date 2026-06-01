import pandas as pd
import matplotlib.pyplot as plt

# 1. 读取 CSV 文件
df = pd.read_csv(r'E:\code\pycharm\datas\linear_data.csv')

# 2. 展示数据（前5行 + 基本信息）
print("===== 前 5 行数据 =====")
print(df.head())

print("\n===== 数据基本信息 =====")
print(df.info())

print("\n===== 统计描述（均值、方差等） =====")
print(df.describe())

# 3. 画图展示线性关系
# 导入绘图库 matplotlib 的pyplot 模块，简写为plt，以后画图都用它
plt.rcParams["font.sans-serif"] = ["SimHei"]  # 正常显示中文      全局参数设置，SimHei 是黑体

# 有些中文字体不认识Unicode负号-  设为False:用普通ASCII负号-
# 作用是 坐标轴负号正常显示，不变为方框
plt.rcParams["axes.unicode_minus"] = False    # 正常显示负号

# 创建画布，长10宽6
plt.figure(figsize=(10, 6))
# 画散点图
plt.scatter(df["c2"], df["c3"], color="#1f77b4", alpha=0.6, label="实际数据")
# 画真实实线
# x:df['c2']  y:2.5*df["c2"] + 10
plt.plot(df["c2"], 2.5*df["c2"] + 10, color="red", linewidth=2, label="真实直线 c3=2.5c2+10")

plt.title("线性回归数据展示", fontsize=14)
plt.xlabel("c2 (特征)", fontsize=12)
plt.ylabel("c3 (标签)", fontsize=12)
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()