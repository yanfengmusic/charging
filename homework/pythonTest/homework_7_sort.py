#!/usr/bin/env python
# -*- coding: utf-8 -*-

__mtime__ = '2020-01-08'

"""
请定义一个函数 mySort，参数为一个列表，参数列表中的元素都是整数.
mySort 函数需要将参数列表中的元素按从小到大排序，最终返回一个新的list。
请按下面算法的思路实现函数：
1. 创建一个新的列表newList
2. 先找出所有元素中最小的，append在newList里面
3. 再找出剩余的所有元素中最小的，append在newList里面
4. 依次类推，直到所有的元素都放到newList里面   
"""
name = "test"
# for循环
alist = [2,5,0,9]
def mySort(alist):
    newList = []
    for i in range(0,len(alist)):
        m = min(alist)
        newList.append(m)
        alist.remove(m)
    return newList

# print(mySort(alist))

# while循环
def my_sort1(inList):
    while len(inList)>0:
        newList = []
        miniData = min(inList)
        newList.append(miniData)
        inList.remove(miniData)
    return newList


# print(__name__)
if __name__ == '__main__':
    # 假设法
    a = mySort(alist)
    print(a)
