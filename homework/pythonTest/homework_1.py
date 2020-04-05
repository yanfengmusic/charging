#!/usr/bin/env python
# -*- coding: utf-8 -*-

__mtime__ = '2020-01-01'

# 拓展篇
# 需求：号段帅选器
# 1、用户控制台输入一个手机号，判断出运营商（移动、联通、电信）
# 2、输入的位数不对，提示用户位数有误
# 3、输入非数字，提示有非法字符

phoneNum = input("请输入手机号")
if len(phoneNum) != 11 :
    print("手机号码位数错误，请输入11位的手机号码")
    if not phoneNum.isdigit():
        print("您输入的内容存在非法字符，请输入数字")
else:
    if not phoneNum.isdigit():
        print("您输入的内容存在非法字符，请输入数字")
    else:
        num = phoneNum[0:3]
        if num in ['130','131','132','133']:
            print("您输入的是联通号码")
        elif num in ['134','135','136','137']:
            print("您输入的是移动号码")
        elif num in ['138','139']:
            print("您输入的是电信号码")
        else:
            print("不存在该号段")



import time
print(time.sleep(5))
import random
print(random.randint(5,10))
import os
import sys
