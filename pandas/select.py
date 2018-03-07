#encoding=utf-8
import pandas as pd
import numpy as np

d1 = {'clo1':[11, 12, 13, 14]}
df1 = pd.DataFrame(data=d1, index=[1, 2, 3, 4])
print df1

print df1['clo1']

d2 = {'clo1':[0.4, 0.3, 0.2, 0.1]}
df2 = pd.DataFrame(data=d2, index=[11, 12, 13, 14])
print df2

print df2.loc[df1['clo1']]

