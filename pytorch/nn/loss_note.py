#encoding=utf-8
import torch
import torch.nn as nn
import torch.nn.functional as F
import math
from torch.autograd import Variable

# http://pytorch.org/docs/master/nn.html#torch.nn.MSELoss
input=Variable(torch.Tensor([[1],[2],[3]]))
# target是一维数组
target=Variable(torch.Tensor([0.1,0.2,0.3]))
# 均方误差
result=F.mse_loss(input, target)
print result
"""
Variable containing:
3.7800
[torch.FloatTensor of size 1]
"""
print ((1-0.1)**2 + (2-0.2)**2 + (3-0.3)**2)/3
"""
3.78
"""
