#!/usr/bin/env python
# -*- coding: utf-8 -*-

__mtime__ = '2020-01-08'

"""
嵌套循环
"""
boys = ['mike','jacl','tom']
girls = ['lisa','lina','mary']

for girl in girls:
    for boy in boys:
        print(girl,boy)

"列表生成式"
beforetax = [1000,1500,1000]
aftertax = []
for one in beforetax:
    if one >= 500:
        aftertax.append(int(one * 0.9))#取整

# 列表生成式：简介优雅
# 一般用于比较简单的列表处理
# 这一种也不好调试

aftertax1 = [int(one*0.9) for one in beforetax if one >=1000]
print(aftertax1)
