#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__:hp

__mtime__ = '2020-03-31'

# pip install rsa
import rsa

pwd = "sdfsdfsdf"
# 每一次加密后的密文是不一样的，而解密是不一样的

# 1实例化加密一个对象
(pubkey,privvkey) = rsa.newkeys(1024)
# 2、用公钥加密
pwd = rsa.encrypt(pwd.encode(),pubkey)
print(pwd.hex())
# 3、私钥解密
depwd = rsa.decrypt(pwd,privvkey)
print(depwd.decode("UTF-8"))


# # 2、用公钥加密
# pwd = rsa.encrypt(pwd.encode(),pubkey)
# print(pwd.hex())
# # 3、私钥解密
# depwd = rsa.decrypt(pwd,privvkey)
# print(depwd.decode("UTF-8"))


