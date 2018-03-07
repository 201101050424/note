#encoding=utf-8
import pandas as pd
import numpy as np
from pd import DataFrame, Series

d1 = {'clo1':[11, 12, 13, 14]}
df1 = pd.DataFrame(data=d1, index=[1, 2, 3, 4])
print df1

print df1['clo1']

d2 = {'clo1':[0.4, 0.3, 0.2, 0.1]}
df2 = pd.DataFrame(data=d2, index=[11, 12, 13, 14])
print df2

print df2.loc[df1['clo1']]

data = pd.DataFrame(np.arange(16).reshape((4,4)),
    index = ['Ohio', 'Colorado', 'Uath', 'New York'], 
    columns = ['one', 'two', 'three', 'four'])
print data

# print data['two']
# print data[['two', 'three']]
# print data[:2]

# 在行上进行索引
print data.ix['Colorado', ['two', 'three']]

s1=Series([7.3, -2.5, 3.4, 1.5], index=['a', 'c', 'd', 'e'])
s2=Series([-2.1, 3.6, -1.5, 4, 3.1], index=['a', 'c', 'e', 'f', 'g'])
print s1+s2

