#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__:hp

__mtime__ = '2020-03-18'

"""
GIL:全局解释器锁（cpython的特性）
就是在这种计算密集型任务时，为了安全性，无论同时进行多少个任务，都只让一个cpu去执行
"""


import threading
import time

def foo():
    num = 0
    for i in range(1000000000):
        num += 1

begin_time = time.time()

t1 = threading.Thread(target=foo)
t2 = threading.Thread(target=foo)
t1.start()
t2.start()

t1.join()
t2.join()

# foo()
# foo()
end_time = time.time()
print("总消耗时长：",end_time-begin_time)
