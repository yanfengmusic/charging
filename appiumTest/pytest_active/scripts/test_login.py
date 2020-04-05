#!/usr/bin/env python
# -*- coding: utf-8 -*-

__mtime__ = '2020-02-28'

import pytest

@pytest.mark.run(order=1)  #修改顺序，这个是run是第三方的 所以需要pip安装
def test_login1():
    print("1")
    # assert True

def test_login2():
    print("2")
    assert False

# @pytest.mark.skipif(True,reson="done")  #跳过
def test_login3():
    print("3")

@pytest.mark.run(order=2)
def test_login4():
    print("4")


# if __name__ == '__main__':
    # pytest.main("-s login.py")
    # test_login()

