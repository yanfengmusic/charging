#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__:hp

__mtime__ = '2020-03-18'

# 进程是并行
# 线程是并发

import threading,time

def foo(something):
    for i in range(10):
        time.sleep(1)
        print("cpu正在:",something)

r1 = threading.Thread(target=foo,args=("看电影",))
r2 = threading.Thread(target=foo,args=("听音乐",))

r1.start()
r2.start()

