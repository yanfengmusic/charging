#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__:hp

__mtime__ = '2020-03-31'

import hashlib

str1 = "sdfsdfsdf"

md5 = hashlib.md5()
md5.update(str1.encode(encoding="utf-8"))
print("MD5加密后的结果为："+ md5.hexdigest())
