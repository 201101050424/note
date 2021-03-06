import numpy as np
#https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.expand_dims.html

x = np.array([1,2])
print x.shape
"""
(2,)
"""

y = np.expand_dims(x, axis=0)
print y.shape
"""
(1,2)
"""

y = np.expand_dims(x, axis=1)
print y.shape
"""
(2,1)
"""
