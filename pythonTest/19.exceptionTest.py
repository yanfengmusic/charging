#!/usr/bin/env python
# -*- coding: utf-8 -*-

__mtime__ = '2020-02-03'

import traceback
# while True:
#     num = input("请输入数字")
#     try:
#         print('100/%s = %s' %(num,100/int(num)))
#     except Exception as info:
#         print('请不要输入0',traceback.format_exc())   #打印异常的出错的位置
#     else:
#         print("else")
#     finally:
#         print("finally")


'''
1.文件读操作：log txt----文件不存在会直接报错
fo = open('f:\hello.xlsx'，'r') 

'''
try:
    fo = open('f:\hello.xlsx','r')
except:
    print("请检查文件路径")

# 自定义异常
class NameTooLongError(Exception):
    error = ''
