#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__:hp

__mtime__ = '2020-03-24'


def handleData(data):
    # 处理消息第二部分吗
    if data == "name":
        dataType = "1"
    else:
        dataType = "2"

    #     处理消息第一部分
    str_len = len(data) + 7
    if len(str(str_len)) < 4:
        data_len = "0" * (4 - len(str(str_len))) + str(str_len)
    else:
        data_len = str(str_len)

    return data_len + "|" + dataType + "|" + data


if __name__ == '__main__':
   a =  handleData("name")
   print(a)
