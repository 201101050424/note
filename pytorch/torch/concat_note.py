import torch
import numpy as np

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
