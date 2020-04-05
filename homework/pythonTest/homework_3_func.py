#!/usr/bin/env python
# -*- coding: utf-8 -*-

__mtime__ = '2020-01-05'

"""

其中包含的 the name is 后面会跟着人名，随后紧跟一个逗号， 这是固定的格式。

其它部分可能都是会变化的，比如，可能是下面这些

A old lady come in, the name is Mary, level 94454

A pretty boy come in, the name is Patrick, level 194

请大家实现一个函数，名为getName，如下所示
def getName(srcStr):
    函数体
该函数的参数srcStr 是上面所描述的格式字符串（只处理一行），该函数需要将其中的人名获取出来，并返回
"""

str1 = "A old lady come in, the name is Mary, level 94454"

def getName(srcStr):
    re = srcStr.split("the name is") #先根据规律按照the name is进行切割
    name = re[1].split(",")[0]#再将切割后结果，以“，”再次切割，并获取切割后的第一个元素，也就是我们想要的名字
    return name
name = getName(str1)
print(name)


