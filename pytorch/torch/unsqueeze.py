import torch
import numpy as np

# http://pytorch.org/docs/master/torch.html

x = torch.Tensor([1, 2, 3, 4])
print x.shape
"""
(4L,)
"""

print torch.unsqueeze(x, 0).shape
"""
(1L, 4L)
"""

x = torch.Tensor([[1], [2], [3], [4]])
x = torch.squeeze(x, 1)
print x
"""
1
2
3
4
[torch.FloatTensor of size 4]
"""
print x.shape
"""
(4L,)
"""
