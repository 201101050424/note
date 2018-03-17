# encoding=utf-8
from annoy import AnnoyIndex
import random

f=40
t=AnnoyIndex(40)
for i in range(1000):
    v=[random.uniform(-1,1) for z in range(f)]
    t.add_item(i, v)

t.build(10)
t.save('./test.ann')

u=AnnoyIndex(f)
u.load('./test.ann')

print dir(u)

target=[0.0]*f

# 结果是item id
result_list = u.get_nns_by_vector(target, 5)
for idx in result_list:
    # 获取具体的向量
    print u.get_item_vector(idx)
