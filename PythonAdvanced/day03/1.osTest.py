#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__:hp

__mtime__ = '2020-03-16'

import os

# 主sys调用外部程序
# 相当于调用cmd
# 返回值 返回退出时响应的值
# os.system("ipconfig")
# os.system("cmd.exe")
retcode = os.system("mspaint")
print(retcode)
