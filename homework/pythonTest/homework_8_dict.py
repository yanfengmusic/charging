#!/usr/bin/env python
# -*- coding: utf-8 -*-

__mtime__ = '2020-01-12'

def func():
    print("step1")
    print("step2")
    print("step3")
    print("step4")
    print("step5")
    print("step6")



def putInfoToDict(fileName):
    fo = open(fileName)
    alist = fo.readlines()
    dict1 = {}
    for one in alist:
        temp = one.strip().split("\n")
        # print(temp)
        time = temp[0].split(",")[0].strip().replace("(","")
        couse = int(temp[0].split(",")[1].strip())
        userid = temp[0].split(",")[2].strip().replace(")","")
        dict0 = {'cid': couse, 'time': time}
        func()
        if userid not in dict1:
            dict1[userid] = [dict0]
        else:
            dict1[userid].append(dict0)
    return dict1

# 完美打印
import pprint
pprint.pprint(putInfoToDict(r"E:\0005_1.txt"))

# import homework_7_sort
# alist = [15,5,0,9]
# print(homework_7_sort.mySort(alist))



import sys
import pprint

# sys.path.append("D:\Tools\PythonProjects\Charging\homework\pythonTest")
# pprint.pprint(sys.path)

# import homework_7_sort
# from homework import homework_7_sort
# from homework.pythonTest import homework_7_sort
# alist = [15,19,4,3,9]
# re = homework_7_sort.mySort(alist)
# print(re)

# import homework_7_sort
# from homework.pythonTest.homework_7_sort import name,mySort
#
# alist = [2,30,5,0,9]
# # a = homework_7_sort.mySort(alist)
# # name = homework_7_sort.name
# print(name)
# print(mySort(alist))

# import sys
# import selenium
# print(sys.path)
