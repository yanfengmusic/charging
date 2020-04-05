#!/usr/bin/env python
# -*- coding: utf-8 -*-

__mtime__ = '2020-01-01'

"""
比较：验证地方在python解释器里面
1、 == 表示值/内容的比较（内容） 【-5,256】
2、 is比较两个对象完全相等（值、地址） 
3、比较字符串，比较的是ASCII码表的值 print('abc' > 'bc')  a 97 A 65  对应位置的比较,前者可以是后者的一个或者一段连续的元素
4、in 和 not in   not > and > or 
4.1在字符串中：前者是后者的一个元素/连续的一段
4.2在列表/元祖中（基本单位都是元素）：前者是后者的一个元素


"""
str1 = "name is tom"
print('n' in str1)
print('name' in str1)

alist = [10,20,30]
alist1 = [[10,20],10,20,30]
print(10 in alist)
print(10,20 in alist)
print([10,20] in  alist)
print([10,20] in  alist1)

"""
条件组合
逻辑条件：且，或，不 and or not    
优先级：not > and > or 
"""
# 练习
"""
2 > 1 and 3 > 2
2 > 1 and 3 > 4
3 > 4 and 2 > 1
2 > 1 or 3 > 2
2 > 1 or 3 > 4
(2 >1 or 3 > 4 ) and 5 > 4
not  3 > 2
not  1 > 2 or 4 >3 
not  (1 > 2 or 4 >3)
1 > 2 or not 4 >3
1 > 2 and  not 4 >3
 
 """
