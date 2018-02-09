#encoding=utf-8
import torch
import torch.nn as nn
import torch.nn.functional as F
import math
from torch.autograd import Variable

# 2个样本，说3分类
input=Variable(torch.FloatTensor([[1,2,3], [1,3,5]]))
# 必须写上维度 http://pytorch.org/docs/master/nn.html#torch.nn.Softmax
print F.softmax(input, 1)
# 等价于
for a in input:
    s=math.exp(a[0])+math.exp(a[1])+math.exp(a[2])
    print math.exp(a[0])/s, math.exp(a[1])/s, math.exp(a[2])/s

print ''

a=F.log_softmax(input, 1)
print a
"""
Variable containing:
-2.4076 -1.4076 -0.4076
-4.1429 -2.1429 -0.1429
[torch.FloatTensor of size 2x3]
"""

# 第几个样本属于哪个label
target=Variable(torch.LongTensor([2,0]))
# The negative log likelihood loss.
# 负log似然
print F.nll_loss(F.log_softmax(input,1), target)
"""
Variable containing:
2.2753
[torch.FloatTensor of size 1]
"""
print (a.data[0][2]+a.data[1][0])*(-1.0)/2
"""
2.2752687186
"""
