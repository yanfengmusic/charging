#!/usr/bin/env python
# -*- coding: utf-8 -*-

__mtime__ = '2020-02-05'

import re
# 1、通配符：.   :一个.只代表一个元素,除了换行符，换行符获取不到
# res = re.findall('s.','songqinsis\n')#1、至少需要有2个必填参数（正则表达式，处理的字符串）2、返回值是列表
# print(res) #['so', 'si']

# 2.（pattern）* 允许模式重复0次或多次
# res = re.findall('son.*','hsongsqins')
# 3.（pattern）* 允许模式重复1次或多次
# res1 = re.findall('son.+','hsongqins')
# print(res)
# print(res1)

# 4、(.*？)(.+?) 匹配0或1个有前面的正则表达式的片段，非贪婪方式

# 5、其他常用：
# \w 匹配所有字母、数字及下划线,表示的是一个元素
# \W 匹配非字母、数字及下划线,表示的是一个元素
# \S 匹配任意空格
# \d 匹配所有的数字 0-9
# ^  匹配是由由什么开头的

# res = re.findall('\w{3}','songqin#_44')  #{3}:表示连续3位的才取
# print(res)
# res = re.findall('\W{1}','songqin#_#44')  #{3}:表示连续3位的才取
# print(res)
# res = re.findall('1*\d{11}','135songqin18712312312#_#44133')  #{3}:表示连续3位的才取
# print(res)


# re常用方法  生成一个re的对象
# res = re.findall('1*\d{11}','135songqin18712312312#_#44133')  #{3}:表示连续3位的才取
# print(res)

# reObject  = re.compile('\d{11}')
# print(reObject.findall('135songqin18712312312#_#44133'))


# re常用修饰符
# re.I 忽略大小写  大小写不敏感 不包括换行符
# re.S 忽略大小写  大小写不敏感 包括换行符
res = re.findall('s.','135sonSo187',re.I)  #{3}:表示连续3位的才取
res1 = re.findall('s.','135sonSo187s\n',re.S)  #{3}:表示连续3位的才取
print(res)
print(res1)

