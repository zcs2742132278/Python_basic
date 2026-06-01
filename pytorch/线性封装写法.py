import matplotlib.pyplot as plt
import pandas as pd
import torch
from torch import nn

# 和tensorflow 中的 Dense 一个意思
# wx + b
model = nn.Linear(1, 1)

# 定义损失函数
loss_fn = nn.MSELoss()

data = pd.read_csv(r'E:\code\pycharm\datas\linear_data.csv')
# 画散点图
plt.scatter(data.c2, data.c3)

plt.xlabel('c2')
plt.ylabel('c3')

X = data.from_numpy(data.c2.values.reshape(-1, 1).type(torch.float32))
Y = data.from_numpy(data.c3.values.reshape(-1, 1).type(torch.float32))

# w
model.parameters()

# 定义优化器
# 优化器的第一个参数必须是要更新的模型中的参数
opt = torch.optim.SGD(model.parameters(),lr=0.001)
w = torch.randn(1, requires_grad=True)
b = torch.zeros(1, requires_grad=True)

# 训练        记住写法
for epoch in range(5000):
    for x,y in zip(X,Y):
        y_pred = torch.matmul(x,w) + b
        loss = loss_fn(y,y_pred)
        # 梯度清零操作
        opt.zero_grad()
        loss.backward()
        # 更新操作
        opt.step()

model.weight
model.bias