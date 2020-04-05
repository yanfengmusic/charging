#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__:hp

__mtime__ = '2020-03-15'

def add(plus1,plus2):
    plus1.encode()

add("1","2")



"""
import random
import time
# 1、random
random.randint(1,5) #整数
random.random() #不用参数的，显示为0-1的小数,处理成整数，可以乘以一个整数
random.random()*1000

# 2.time  返回的是从1970年开始截止到调用时的毫秒数 单位为ms
print(time.time)


"""
import time
import random

# re = time.time()
# re1 = time.strftime("%Y_%m_%d %H:%M:%S")
r = random.randint(1,5)
r1 = random.random()*100
print(r1)
