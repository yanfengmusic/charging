#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__:hp

__mtime__ = '2020-03-18'



import threading,time

# def foo(something):
#     for i in range(10):
#         time.sleep(1)
#         print(something)
#
# r1 = threading.Thread(target=foo,args=("看电影",))
# r2 = threading.Thread(target=foo,args=("听音乐",))
#
# # 设置守护线程，必须在执行前设置，主线程运行结束后，守护线程就不执行了
# r1.setDaemon(True)
# r2.setDaemon(True)
#
# r1.start()
# r2.start()
#
# for i in range(5):
#     time.sleep(1)
#
# print("启动数据检查")

a = []
def foo():
    while True:
        a.append("1")
        print("生产一个数据")
        time.sleep(1)

r1 = threading.Thread(target=foo)
# r1.setDaemon(True)
r1.start()

for i in range(10):
    if a:
        a.remove("1")
        print("消费了一个数据")
        time.sleep(1)
print("不需要再消费数据了")
