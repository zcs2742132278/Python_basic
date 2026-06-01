# pytorch中的张量和tensorflow的tensor是一样，名字都一样
# pytorch中的张量也叫tensor       tensor多维数组的意思
# tensor和numpy中的ndarray也是一个意思，只不过tensor可以再GPU上加速计算

# 张量是torch中数据的 数组、矩阵、容器
import numpy as np
import torch

# 创建tensor
print(torch.tensor([6, 2],dtype=torch.int32))
print(torch.tensor((6,2)))
print(torch.tensor(np.array([6,2])))

print(('*' * 30))
# 快速创建torch的方法，和numpy中的routines方法一样
# ones  zeros  full  eye  random.randn  random.normal  arange  random.rand  random.random
# 创建一个0到1之间的随机数组成的tensor
print(torch.rand(2, 3))         # 生成一个 2行 3列  的数组
print(torch.rand((2, 3)))

print(('*' * 30))
# 标准正态分布  均值为0 方差为1 大部分数在-1到1之间(-无穷大 到 正无穷大)
print(torch.randn(2, 3))

print(('*' * 30))

print(torch.zeros(2, 3))

print(torch.ones(2, 3))


print(('*' * 30))

x = torch.ones(2,3,4)

print(x)
# 查看张量形状，尺寸，大小
print(x.shape)
print(x.size())
print(x.size(0))
print(x.size(1))
print(x.size(2))


print(('*' * 30))

# 创建tensor的时候可以指定数据类型
print(torch.tensor([6, 2], dtype=torch.float32))


print(('*' * 30))
# tensorflow 不能直接用tensor方法创建tensor
# tensorflow 提供了constant，Variable
# keras：deeplearning for human
# 正态分布
n = np.random.randn(2,3)        # array
print(n)
# 转化为 torch
a = torch.from_numpy(n)
print(a)
# 转化为numpy
print(a.numpy())

# tensor运算规则和numpy的ndarray 很像
# 和单个数字运算
print(('*' * 30)+'张量运算')
t1 = torch.ones(2,3)
print(t1 + 3)
print(torch.add(t1,3))


print(('*' * 30)+'张量运算')
x1 = torch.ones(2,3)
print(x1)
# 对应位置的元素相加、element-wise操作 残差网络的+ 就是element-wise相加
print(t1 + x1)
print(t1.add(x1))
print(t1)
print(('*' * 30)+'张量运算')
# .add()有输出，不改变原始值,.add_()有输出改变原始值
t1.add_(x1)
print(t1)

# torch.inverse () = 求方阵的逆矩阵        只有方阵才有逆，方阵是2*2 3*3 4*4
print(torch.ones(2,2))
i = torch.ones(2,2)
print(i)
# torch.ones(*,*)没有逆
j = torch.tensor([
    [2.,3.,4.],
    [3.,5.,1.],
    [5.,2.,1.]
])
print("j的逆矩阵：\n", torch.inverse(j))

# 1. 定义2阶方阵
A = torch.tensor([[1., 2.],
                  [3., 4.]])

# 2. 求逆矩阵
A_inv = torch.inverse(A)
print("A的逆矩阵：\n", A_inv)

# 3. 矩阵相乘，验证结果 = 单位矩阵
res = torch.matmul(A, A_inv)
print("A × A⁻¹：\n", res)

t2 = torch.tensor([[2.,3.,4.],
                   [3.,5.,6.]])

print("变换形状\n")
print(t2.reshape(3, 2))
print(t2)
print(t2.view(3, 2))
print("聚合操作\n")
print(t2.mean())
print(t2.sum)
