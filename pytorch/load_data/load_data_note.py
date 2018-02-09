#encoding=utf-8
import numpy as np
from tqdm import tqdm
from torch.utils.data import Dataset, DataLoader

"""
数据集类，代表数据，自己定义的数据集类必须继承Dataset
"""
class MyDataset(Dataset):
    """
    必须实现三个函数
    """
    def __init__(self):
        self.data=np.eye(1024,2)
    def __len__(self):
        return self.data.shape[0]
    def __getitem__(self, idx):
        return self.data[idx]

dataset=MyDataset()
"""
DataLoader是遍历Dataset的迭代器，主要具备以下三个功能
1. batching the data
2. shuffling the data
3. 并行读取
"""
dataloader=DataLoader(dataset, batch_size=128, shuffle=True, num_workers=4)
num=0
for batch in tqdm(dataloader):
    num+=1
    assert batch.shape==(128,2)
    print batch.shape
print num
assert num==8
