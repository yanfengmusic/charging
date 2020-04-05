#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__:hp

__mtime__ = '2020-03-18'

# 比如说进入数据库查询，需要等待
# 比如说一个请求，需要等待服务器的响应
# 比如文件读写
# 只要你的任务有等待的 就是IO任务
# 我们这里用sleep()来模拟

# 串行：从上往下，排队执行

import threading
import time

def foo(something):
    print(something)
    time.sleep(2)

begin_time = time.time()

t1 = threading.Thread(target=foo,args=["磁盘写入100M数据"])
t2 = threading.Thread(target=foo,args=["cpu去做其他事情"])
t1.start()
t2.start()

t1.join()
t2.join()

end_time = time.time()
print("总消耗时长：",end_time-begin_time)


# begin_time = time.time()
# foo("磁盘写入100M数据")
# foo("cpu去做其他事情")
# end_time = time.time()
# print("总消耗时长：",end_time-begin_time)
#
