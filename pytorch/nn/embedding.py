#encoding=utf-8
import torch.nn as nn
import torch.nn.functional as F
import torch
import numpy as np
from torch.autograd import Variable

embedding=nn.Embedding(1000, 10)
input=Variable(torch.LongTensor([[1,2,3,5], [4,3,2,9]]))
output=embedding(input)
print output.shape
"""
(2L, 4L, 10L)
"""
