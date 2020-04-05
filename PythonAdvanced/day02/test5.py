#!/usr/bin/env python
# -*- coding: utf-8 -*-

__mtime__ = '2020-03-15'

import chardet

# 如果某一个文件
# 获取文件编码类型的函数
def get_encoding(file):
    #以二进制的方式读取，获取字节数据去检测类型
    with open(file,"rb")as f:
        data = f.read(1024)
        return chardet.detect(data) #返回需要的文件编码信息,因为编码集有可能是重合的，就比如说同样的一个字符既属于是utf8,同时也可以用gbk来解码，也就是说有一定的相似率，那么就存在结果不稳定的情况。

file_name = "./a.txt"
encoding_data = get_encoding(file_name)
print(encoding_data)
