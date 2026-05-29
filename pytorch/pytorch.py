import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset

# ============================================================
# 1. 张量基础操作
# ============================================================
print("=" * 50)
print("1. 张量基础操作")
print("=" * 50)

# 创建张量
a = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32)
b = torch.randn(2, 2)
print(f"张量 a:\n{a}")
print(f"随机张量 b:\n{b}")

# 张量运算
print(f"a + b:\n{a + b}")
print(f"a @ b (矩阵乘法):\n{a @ b}")
print(f"a 的形状: {a.shape}, 数据类型: {a.dtype}")

# GPU 检测
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"使用设备: {device}")

# ============================================================
# 2. 自动求导
# ============================================================
print("\n" + "=" * 50)
print("2. 自动求导 (Autograd)")
print("=" * 50)

x = torch.tensor([2.0], requires_grad=True)
y = x ** 3 + 2 * x ** 2 + 1
y.backward()
print(f"y = x^3 + 2x^2 + 1, 在 x=2 时 dy/dx = {x.grad.item()}")  # 期望: 3*4 + 4*2 = 20

# ============================================================
# 3. 构建简单的神经网络
# ============================================================
print("\n" + "=" * 50)
print("3. 构建简单的神经网络")
print("=" * 50)


class SimpleNet(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super().__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return x


model = SimpleNet(input_size=10, hidden_size=20, output_size=1).to(device)
print(model)
print(f"模型参数量: {sum(p.numel() for p in model.parameters())}")

# ============================================================
# 4. 训练示例：线性回归
# ============================================================
print("\n" + "=" * 50)
print("4. 训练示例：线性回归")
print("=" * 50)

torch.manual_seed(42)

# 生成模拟数据: y = 3x + 2 + 噪声
X = torch.linspace(-10, 10, 200).reshape(-1, 1)
y = 3 * X + 2 + torch.randn(X.shape) * 3

dataset = TensorDataset(X, y)
dataloader = DataLoader(dataset, batch_size=32, shuffle=True)

# 单层线性模型
linear_model = nn.Linear(1, 1).to(device)
criterion = nn.MSELoss()
optimizer = optim.SGD(linear_model.parameters(), lr=0.01)

epochs = 100
for epoch in range(epochs):
    for batch_X, batch_y in dataloader:
        batch_X, batch_y = batch_X.to(device), batch_y.to(device)
        pred = linear_model(batch_X)
        loss = criterion(pred, batch_y)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    if (epoch + 1) % 20 == 0:
        print(f"Epoch [{epoch + 1}/{epochs}], Loss: {loss.item():.4f}")

# 检查学到的参数
w, b = linear_model.weight.item(), linear_model.bias.item()
print(f"\n真实参数: y = 3x + 2")
print(f"学习参数: y = {w:.2f}x + {b:.2f}")

# ============================================================
# 5. 模型保存与加载
# ============================================================
print("\n" + "=" * 50)
print("5. 模型保存与加载")
print("=" * 50)

torch.save(linear_model.state_dict(), "linear_model.pth")
print("模型已保存为 linear_model.pth")

loaded_model = nn.Linear(1, 1)
loaded_model.load_state_dict(torch.load("linear_model.pth", weights_only=True))
loaded_model.eval()
print("模型已加载")

# 测试预测
with torch.no_grad():
    test_x = torch.tensor([[5.0]])
    test_pred = loaded_model(test_x)
    print(f"输入 x=5, 预测 y={test_pred.item():.2f}")