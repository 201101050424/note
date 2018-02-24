#encoding=utf-8
import torch.nn as nn
import torch
from torch.autograd import Variable

m = nn.Conv1d(5, 2, 2)
# wordvector维度5，filter个数10，filter每次侦测连续的2个词
m.weight=torch.nn.Parameter(torch.ones(2, 5, 2))
m.bias=torch.nn.Parameter(torch.ones(2))

input = Variable(torch.Tensor(
        [
            [
                [1, 2, 3, 5],
                [1, 2, 3, 5],
                [1, 2, 3, 5],
                [1, 2, 3, 5],
                [1, 2, 3, 5],
            ],
        ]
    )
)

feature_maps = m(input)
print feature_maps
"""
Variable containing:
(0 ,.,.) = 
16  26  41
16  26  41
[torch.FloatTensor of size 1x2x3]
"""
