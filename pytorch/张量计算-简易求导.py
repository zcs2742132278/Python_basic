import matplotlib.pyplot as plt
import pandas as pd
import torch

data = pd.read_csv(r'E:\code\pycharm\datas\linear_data.csv')

# 修复1: 使用 .to_numpy() 替代 .values，确保数组可写
X = torch.tensor(data.c2.to_numpy().reshape(-1, 1), dtype=torch.float32)
Y = torch.tensor(data.c3.to_numpy().reshape(-1, 1), dtype=torch.float32)

# 修复2: 对数据做归一化（标准化到 0均值/1标准差），防止梯度爆炸
X_mean, X_std = X.mean(), X.std()
Y_mean, Y_std = Y.mean(), Y.std()
X_norm = (X - X_mean) / X_std
Y_norm = (Y - Y_mean) / Y_std

# 修复3: 降低学习率（归一化后 0.01 是合适的）
learning_rate = 0.01

# requires_grad=True: 我要对这个变量计算梯度！要用它进行反向传播/梯度下降/训练模型！
w = torch.randn(1, requires_grad=True)
b = torch.zeros(1, requires_grad=True)

# 训练过程
for epoch in range(500):  # 归一化后收敛更快，500 轮足够
    for x, y in zip(X_norm, Y_norm):
        y_pred = torch.matmul(x, w) + b
        loss = (y - y_pred).pow(2).mean()  # 修复4: 用 mean 替代 sum，loss 数值更稳定

        # PyTorch 对一个变量多次求导，求导结果会累加起来
        if w.grad is not None:
            w.grad.zero_()  # 修复5: 直接 .zero_()，不用 .data
        if b.grad is not None:
            b.grad.zero_()

        # 反向传播
        loss.backward()

        # 更新参数（torch.no_grad 内操作不会被求导）
        with torch.no_grad():
            w -= w.grad * learning_rate  # 修复6: 不需要 .data
            b -= b.grad * learning_rate

# 反归一化：把归一化后的预测值映射回原始数据空间
# y_norm = X_norm * w + b  →  y_origin = y_norm * Y_std + Y_mean
with torch.no_grad():
    Y_pred = ((X_norm @ w + b) * Y_std + Y_mean).reshape(-1, 1)  # 保持 (N,1) 形状，避免广播问题

# 计算 R² 分数评估模型效果
ss_res = ((Y - Y_pred) ** 2).sum()
ss_tot = ((Y - Y.mean()) ** 2).sum()
r2 = 1 - ss_res / ss_tot
print(f'训练完成: w={w.item():.4f}, b={b.item():.4f}, R²={r2.item():.4f}')

# 画散点图
plt.scatter(data.c2, data.c3, label='实际数据')
plt.plot(X.numpy().flatten(), Y_pred.numpy().flatten(), c='r', label='预测直线')
plt.xlabel('c2')
plt.ylabel('c3')
plt.legend()
plt.show()
