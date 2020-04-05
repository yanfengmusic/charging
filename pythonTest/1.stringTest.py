#!/usr/bin/env python
# -*- coding: utf-8 -*-

__mtime__ = '2019-12-30'

# 注释、取消注释 ctrl+/
# 字符串是用任意一组单引号或者双引号标识的
# 单引号和双引号可以包含使用，比如双引号包着单引号或者单引号包着双引号
# 三引号，表示多行字符串，也可以表示注释
# info = 'name is tom'
# print(info)

var1 = """what's your name"""
print(var1)
'''
我是注释

'''
# 字符串拼接，字符串后面必须跟字符串
# +号看的是前面的变量的类型，如果前面是数字，就变成了加数的加，如果前面是字符串，加号就变成了拼接，字符串只能和字符串拼接
# print(5 + 'hello')
# print('hello'+5)
# print('hello'+'s')

# print(5*'hello')

# sequence操作
# 字符串的特性，被称为sequence（序列）
# 一个序列，若干个元素组成
# 与java一样，字符串的底层就是一个数组，所以这个字符串也会有下标的概念，以及长度等方法

info = 'abcdef'
# num = len(info)
# print(num)
# print(info[num-1])
# print(info[len(info)-1])
# 负下标 从右往左 -1 -n
# print(info[-1],info[-len(info)])
# print(info[0],info[-1])

# 切片 截取某一段字符串 左闭右开,不会影响原字符串
# print(info[1:1+2])
# print(info[:3]) # 从0开始,取到2
# print(info[3:])#从3开始取到最后
# print(info[::1])
# print(info[::-1])










