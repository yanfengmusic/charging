#!/usr/bin/env python
# -*- coding: utf-8 -*-

__mtime__ = '2020-01-01'

# if单语句
# if else
# if elif
# if条件为真的：1、非0数值，非空字符串，非空元祖，非空列表
score = 80
if score >= 90:
    pass #空语句，避免语法报错
    print("A")
elif score >= 80:
    print("B")
elif score >= 60:
    print("C")
else:
    print("不及格")
print("over")

# if 嵌套
score = 80
if score >= 60:
    if score >= 90:
        print("A")
else:
    print("不及格")

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
elif len(phoneNum) == 11:
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
            print("over")


a = 2
b = 3
if a > 1:
      if b > 2:
        print("ok")
if a>1 and b>2:
    print("ok")

