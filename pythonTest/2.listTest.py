#!/usr/bin/env python
# -*- coding: utf-8 -*-

__mtime__ = '2019-12-30'

# 列表 也就是我们之前说的数组 可以存储任意类型 也是一种序列类型 所以也有下标，可以做切片

# alist = [10,3.14,'hello',[100,200]]
# print(type(alist))
#
# print(alist[0])
# print(alist[-1][0])
# print(alist[:5:2])
# print(len(alist))
# print(100 in alist)
# print(100 in alist[-1])

# 常用操作
alist = [10,20,30,40]
# 1、根据下标进行查询
print(alist[0])
# 2、修改
alist[0] = 50
print(alist)
# 3、增加元素
# 3-1 append(需要增加的元素) 在尾部追加
# 3-2 insert(需要插入的位置下标,插入的值）
# 3-3 del 使用下标删除,永久删除
# 3-4 pop 有返回值，返回删除的值
# 3-5 remove(删除的值),每次只能删一个，第一次出现的值,效率是最低的
alist.append(50)
print(alist)
alist.insert(1,50)
print(alist)
print(id(list))
del alist[0],alist[1]    # 删除的时候，下标是在变化的
print(id(list))
print(alist)
del alist[1:1+2]

a = alist.pop(0)
print(a)

print(alist)
alist.remove(50)
print(alist)

"""
删除重复的操作
"""
while 20 in alist:
    alist.remove(20)
print(alist)

# 获取下标
alist = [10,20]
print(alist.index(20))

# 合并列表
print(alist+[30,40])  #临时拼接，另存新地址，不会改变原来的列表
alist.extend([30,40]) # 拓展列表，改变原来的元素
print(alist)


a = [(1,2),3,"strdd"]
print(a)
tup = (1,)
print(tup)

