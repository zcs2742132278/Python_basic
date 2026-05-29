import torch

#
# print(torch.cuda.get_device_name(0))

# 查看pytorch版本
print(('Pytorch 版本:', torch.__version__))
# 查看本机显卡是否存在
print(('CUDA 是否可用:', torch.cuda.is_available()))
if torch.cuda.is_available():
    print(('显卡型号:', torch.cuda.get_device_name(0)))