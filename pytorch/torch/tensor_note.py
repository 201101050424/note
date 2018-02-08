import torch
import numpy as np

a=np.ones(5)
print a.shape
b=torch.from_numpy(a)
print b
