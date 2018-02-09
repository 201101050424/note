#encoding=utf-8
import torch.nn as nn
import torch.nn.functional as F
import torch
import numpy as np
from torch.autograd import Variable

# 5个样本，每个样本序列长度10，单item维度50
input=Variable(torch.randn(5,10,50))
# 单item维度、单个隐层lstm神经元个数、lstm层数，这里初始化的时候并没有序列长度相关参数
lstm=nn.LSTM(50, 100, 3, batch_first=True)
output, (h, c) = lstm(input)
print output.shape
"""
(5L, 10L, 100L)
5个样本，每个样本序列长度10，单item的维度和隐层一样都变成了100
"""
print h.shape
"""
(3L, 5L, 100L)
"""
print c.shape
"""
(3L, 5L, 100L)
"""
