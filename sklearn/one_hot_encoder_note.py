import numpy as np
from sklearn.preprocessing import OneHotEncoder
enc = OneHotEncoder()
enc.fit(np.array([[1], [2], [3], [4], [5], [1], [2]]))

print enc.transform([[1], [4], [3]]).toarray()
