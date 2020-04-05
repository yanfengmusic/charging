#!/usr/bin/env python
# -*- coding: utf-8 -*-

__mtime__ = '2020-01-06'

# students = ['mike','jace','mary']
# idx = 0
# while idx < len(students):
#     print(students[idx],end="")
#     idx += 1
#
# for name in students:
#     print(name,end="\n")

# for one in range(0,5):#左闭右开
#     print(one,end="")
# for one in range(0,5,2):#左闭右开,跟切片时一样，隔一个一取
#     print(one,end="")

# for one in range(0,5,-1):#不报错，也取不到值的
#     print(one,end="")
#
# for one in range(5,0,-1):#
#     print(one,end="")

"""
while使用场景：
1、根据条件结束
2、while True: if break :当一个场景不知道循环次数，但是循环是通过条件结束


for使用场景：
1、遍历操作
2、需要指定遍历次数
"""

for one in range(1,5):
    if one == 3:
        # break #终止，结束本层循环
        continue#结束本次循环，继续下次循环
    # return是函数的结束
    print(one)

# 注释
# 1、ctrl+/
# 2、把代码圈出来  #-------------------这是xxx代码-----------
# 3、看函数的功能：print(print._doc_)
# 4、在函数下面加3个点注释
print(print.__doc__)

def get_sum(start,end,step=1):
    """
    :param start:
    :param end:
    :param step:
    :return:
    """
    sum = 0
    cnt = start  # 从1开始累加
    while cnt <= end:
        sum += cnt
        cnt += step
    print(sum)
    return sum

print(get_sum.__doc__)
