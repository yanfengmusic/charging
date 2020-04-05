#!/usr/bin/env python
# -*- coding: utf-8 -*-

__mtime__ = '2020-01-06'

# while True: #while 3>2
#     print("我在循环了")

"""
需求：
1、求和的基本用法  while
2、想经常使用，使用函数/方法
3、函数/方法调用者想算自定义的和----增加接口的概念（形参）
4、求指定范围内的基数、偶数的和
5、求等差数列
6、使用缺省函数
"""

# 求1+....+100的和
# sum = 0
# cnt = 1 #从1开始累加
# while cnt<=100:
#     sum += cnt
#     cnt += 1
# print(sum)

# def get_sum():
#     sum = 0
#     cnt = 1  # 从1开始累加
#     while cnt <= 100:
#         sum += cnt
#         cnt += 1
#     print(sum)
#     return sum
#
# get_sum()

# def get_sum(start,end):
#     sum = 0
#     cnt = start  # 从1开始累加
#     while cnt <= end:
#         sum += cnt
#         cnt += 1
#     print(sum)
#     return sum
#
# get_sum(1,100)


# def get_sum(start,end,step):
#     sum = 0
#     cnt = start  # 从1开始累加
#     while cnt <= end:
#         sum += cnt
#         cnt += step
#     print(sum)
#     return sum
#
# get_sum(2,10,2)


# def get_sum(start,end,step):
#     sum = 0
#     cnt = start  # 从1开始累加
#     while cnt <= end:
#         sum += cnt
#         cnt += step
#     print(sum)
#     return sum
#
# get_sum(2,10,2)


# def get_sum(start,end,step=1):
#     sum = 0
#     cnt = start  # 从1开始累加
#     while cnt <= end:
#         sum += cnt
#         cnt += step
#     print(sum)
#     return sum
#
# get_sum(2,10)





