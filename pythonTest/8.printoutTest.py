#!/usr/bin/env python
# -*- coding: utf-8 -*-

__mtime__ = '2020-01-06'

Myage = 13
my_name = 'xiaoming'
my_height = 187.3
print("小明今年%d岁" % Myage)
print("名字是%s" %my_name)
print('身高是%f' %my_height) #不写默认是6位
print('身高是%.2f' %my_height)

# 如果想要格式化输入bool类型
# 1、把bool类型看成字符串类型
# 2、把字符串了你才能够看成数字类型
is_boy = True
print("是男孩吗：%s" %is_boy)
print("是男孩吗：%d" %is_boy)

print("hello\nworld")
