#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__:hp

__mtime__ = '2020-03-18'

import threading,time

def foo(something):
    for i in range(10):
        time.sleep(1)
        print("cpu正在:",something)

# 创建实例线程 target指向实例的对象 args为实例对象传参
r1 = threading.Thread(target=foo,args=("看电影",))
r2 = threading.Thread(target=foo,args=("听音乐",))

r1.start()
r2.start()

# join阻塞主线程 只有当子线程完成之后 主线程才会运行
r1.join()
r2.join()
print("启动数据检查")

