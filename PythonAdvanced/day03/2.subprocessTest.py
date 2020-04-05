#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__:hp

__mtime__ = '2020-03-16'

import subprocess

"""
# 将结果以字节形式返回 也就是byte类型
output_bytes = subprocess.check_output("ipconfig")
print(output_bytes)
print(output_bytes.decode("gbk"))

"""

# subprocess.Popen("ipconfig")
# subprocess.Popen("mspaint")
# print("after")


from subprocess import Popen,PIPE

# 输出和输出重定向
# child = Popen("ipconfig")
# child.wait()
# child = Popen("ipconfig",
#               stdout = PIPE,
#               encoding="gbk")
# out,eror = child.communicate()
# print(out)

# 输入重定向
child = Popen("python ioTest.py",
              # stdout = PIPE,
              stdin= PIPE,
              # stderr=PIPE,
              encoding="gbk")
out,eror = child.communicate("\n".join(["1","2"]))
print(out)
