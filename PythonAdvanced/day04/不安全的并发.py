#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__:hp

__mtime__ = '2020-03-18'

import threading
import time


balance = 500 #银行卡账户余额
lock = threading.Lock() #声明一把锁

# 操作账户余额
def foo(num):

    global balance
    lock.acquire()
    account_balance = balance
    time.sleep(1)
    # 进行了一系列复杂的操作，计算出了一个结果
    account_balance = account_balance + num
    # 将计算结果传递回去
    balance = account_balance
    lock.release()
#消费200
t1 = threading.Thread(target=foo,args=[-300])
# 收入10000
t2 = threading.Thread(target=foo,args=[10000])

t1.start()
t2.start()

# 等所有的线程运行结束后，看下余额为多少
t1.join()
t2.join()

print("balance:",balance)

