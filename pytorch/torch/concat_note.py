#encoding=utf-8
import torch
import numpy as np
from torch.autograd import Variable

# http://pytorch.org/docs/master/torch.html

a = torch.from_numpy(np.array([[1, 2], [3, 4]]))
b = torch.cat([a, a, a], 0)
print b
"""
1  2
3  4
1  2
3  4
1  2
3  4
[torch.LongTensor of size 6x2]
"""

a = torch.from_numpy(np.array([[1, 2], [3, 4]]))
b = torch.cat([a, a, a], 1)
print b
"""
1  2  1  2  1  2
3  4  3  4  3  4
[torch.LongTensor of size 2x6]
"""

a = torch.from_numpy(np.array([[1, 2], [3, 4]]))
b = torch.from_numpy(np.array([[1, 2, 3], [3, 4, 6]]))
# 把列拼接起来
print torch.cat([a, b], 1)
"""
1  2  1  2  3
3  4  3  4  6
[torch.LongTensor of size 2x5]
"""

# 对Variable同样适用
a = Variable(torch.from_numpy(np.array([[1, 2], [3, 4]])))
b = Variable(torch.from_numpy(np.array([[1, 2, 3], [3, 4, 6]])))
print torch.cat([a, b], 1)
"""
Variable containing:
1  2  1  2  3
3  4  3  4  6
[torch.LongTensor of size 2x5]
"""

a = torch.Tensor([[1,2], [3,4]]).long()
b = torch.Tensor([[1,2], [3,4]]).float()
print torch.cat([a, b], 1)
"""
类型不一样会报错
"""
