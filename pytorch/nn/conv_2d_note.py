import torch.nn as nn
import torch.nn.functional as F
import torch
import numpy as np
from torch.autograd import Variable

a=np.array(
[
[
	[
		[1,2,3],
		[4,5,6],
	],
	[
		[2,1,1],
		[5,3,6],
	],
	[
		[1,1,2],
		[3,4,7],
	],
]
])
print a.shape
b=torch.from_numpy(a)
b=Variable(b)
filter=torch.eye(3)
print filter.shape
#filter=filter.unsqueeze(0)
filter=torch.stack([filter, filter], 0)
print filter
filter=Variable(torch.eye(2))

#print filter
#c=F.conv2d(3, 2, 2)
