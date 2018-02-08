import torch
import numpy as np

# http://pytorch.org/docs/master/torch.html

a=torch.from_numpy(np.array([[1,2],[3,4]]))
b=torch.stack([a, a,a,a], 0)
print b
"""
(0 ,.,.) = 
  1  2
  3  4

(1 ,.,.) = 
  1  2
  3  4

(2 ,.,.) = 
  1  2
  3  4

(3 ,.,.) = 
  1  2
  3  4
[torch.LongTensor of size 4x2x2]
"""

b=torch.stack([a,a,a,a], 1)
print b
"""
(0 ,.,.) = 
  1  2
  1  2
  1  2
  1  2

(1 ,.,.) = 
  3  4
  3  4
  3  4
  3  4
[torch.LongTensor of size 2x4x2]
"""

b=torch.stack([a,a,a,a], 2)
print b
"""
(0 ,.,.) = 
  1  1  1  1
  2  2  2  2

(1 ,.,.) = 
  3  3  3  3
  4  4  4  4
[torch.LongTensor of size 2x2x4]
"""
