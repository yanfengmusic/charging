#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__:hp

__mtime__ = '2020-03-29'

import os

def checkScore(num):
    assert num > 50


def openCalc():
    os.system('calc')

def openMspaint():
    os.system('mspaint')

def printargs(*args,**kwargs):

    if len(args)==0:
        print("*** no args ***")
    else:
        print("*** args are ***")
        print("-------------------------")
        for one in args:
            print(repr(one))
    if len(kwargs) == 0:
        print("*** no kwargs ***")
    else:
        print("*** kwargs ***")
        print("-------------------------")
        for k,v in kwargs.items():
            print(repr(k)+':'+repr(v))

def returnList():
    return [1,2,3,4]

def returnDict():
    return {'key1':123,'key2':'456'}


if __name__ == '__main__':
    # openCalc()
    printargs(k=15)
