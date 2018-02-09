#encoding=utf-8
import torch
import torch.optim as optim
import time
from torch.autograd import Variable

param=Variable(torch.FloatTensor([[1], [2]]), requires_grad=True)

# 把需要优化的参数传递给优化器
optimizer=optim.SGD([param], lr=1e-1, momentum=0.9)
step=0
while True:
    optimizer.zero_grad()
    # 计算loss值，计算图的终点
    out=torch.mul(param, param).sum()
    # 求梯度
    out.backward()
    # 更新参数
    optimizer.step()
    print 'step=%s value=%f' % (step,out.data[0])
    step+=1
    time.sleep(0.1)
