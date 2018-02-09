#encoding=utf-8
import torch
from torch.autograd import Variable

input=Variable(torch.Tensor([[2],[1]]))
# 默认requires_grand是False，不求导，实践中网络的权重都是需要求导的
a=Variable(torch.Tensor([[3],[4]]), requires_grad=True)
b=Variable(torch.Tensor([[5],[3]]), requires_grad=True)

out=torch.transpose(a*a, 0, 1).mm(input)+torch.transpose(b, 0, 1).mm(input)
print out
"""
Variable containing:
47
[torch.FloatTensor of size 1x1]
"""

out.backward()

"""
out=2*x_1^2+y_1^2+2*x_2+y_2
对x_1求导4*x_1=4*3=12
对y_1求导2*y_1=2*4=8
对x_2求导2
对y_2求导1
"""
print a.grad
"""
Variable containing:
12
8
[torch.FloatTensor of size 2x1]
"""
print b.grad
"""
Variable containing:
2
1
[torch.FloatTensor of size 2x1]
"""
