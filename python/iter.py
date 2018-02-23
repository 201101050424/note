#encoding=utf-8
# 使用iter函数生成一个迭代器
iterator = iter([1,2,3,4])
print type(iterator)

print iterator.next()
print iterator.next()
print iterator.next()
print iterator.next()

# 无元素抛StopIteration异常
print iterator.next()
