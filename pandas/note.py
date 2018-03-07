import pandas as pd

p=pd.read_csv('./data', sep='\t')

print type(p['c2'])
"""
<class 'pandas.core.series.Series'>
"""

print p[p['c2']>2]
"""
   c1   c2  c3
1   4  5.0   6
"""

print type(p[p['c2']>2])
"""
<class 'pandas.core.frame.DataFrame'>
"""

print p['c2'].isnull()
"""
0    False
1    False
2     True
Name: c2, dtype: bool
"""

print type(p['c2'].isnull())
"""
<class 'pandas.core.series.Series'>
"""

p['c4']=p['c1'].apply(lambda x:x**2)
print p
"""
   c1   c2  c3  c4
0   1  2.0   3   1
1   4  5.0   6  16
2   5  NaN   6  25
"""

print p['c1'].values
print p['c1'].values.shape
print type(p['c1'].values)
"""
[1 4 5]
(3,)
<type 'numpy.ndarray'>
"""
