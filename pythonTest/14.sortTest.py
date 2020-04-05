#!/usr/bin/env python
# -*- coding: utf-8 -*-

__mtime__ = '2020-01-08'

"""排序算法"""

# alist = [9,2,6,0]
# alist.sort() #升序
# alist.sort(reverse=True) #降序
# print(alist[::-1]) #使用切片降序

# 冒泡排序，找n-1次最大值，两两元素相比较，大的往后移动
alist = [9,2,6,0]
for i in range(0,len(alist)-1):
    for j in range(0,len(alist)-1-i):
        if alist[j] > alist[j+1]:
            alist[j],alist[j+1] = alist[j+1],alist[j]
print(alist)


