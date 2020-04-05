#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
__mtime__ = '2020-02-28'

def test_loin():
    print("正在登陆")
def test_login2():
    print("xxxx")
if __name__ == '__main__':
    # 代码运行方式
    pytest.main(["-s","demo.py"])
    # pytest.main("-s demo1.py")
#     命令行运行方式
# pytest -s demo.py
