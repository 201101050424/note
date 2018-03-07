import pandas as pd
import numpy as np

p=pd.read_csv('./text', sep='\t')

print p['c1'].str.lower()
"""
0     a
1    aa
Name: c1, dtype: object
"""
print type(p['c1'].str.lower())
"""
<class 'pandas.core.series.Series'>
"""

all_text=np.hstack([p['c1'], p['c2']])
print all_text
"""
['a' 'aa' 'b' 'bb']
"""
print type(all_text)
"""
<type 'numpy.ndarray'>
"""

print np.vstack([p['c1'], p['c2']])
"""
[['a' 'aa']
 ['b' 'bb']]
"""
print type(np.vstack([p['c1'], p['c2']]))
"""
<type 'numpy.ndarray'>
"""
