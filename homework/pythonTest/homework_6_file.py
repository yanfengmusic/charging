#!/usr/bin/env python
# -*- coding: utf-8 -*-

__mtime__ = '2020-01-09'

"""
现有文件1（如下，请保存到文件file1.txt中）， 记录了公司员工的薪资，其内容格式如下
name: Jack   ;    salary:  12000
 name :Mike ; salary:  12300
name: Luk ;   salary:  10030
  name :Tim ;  salary:   9000
name: John ;    salary:  12000
name: Lisa ;    salary:   11000
每个员工一行，记录了员工的姓名和薪资，
每行记录 原始文件中并不对齐，中间有或多或少的空格
现要求实现一个python程序，计算出所有员工的税后工资（薪资的90%）和扣税明细，
以如下格式存入新的文件 file2.txt中，如下所示
name: Jack   ;    salary:  12000 ;  tax: 1200 ; income:  10800
name: Mike   ;    salary:  12300 ;  tax: 1230 ; income:  11070
name: Luk    ;    salary:  10030 ;  tax: 1003 ; income:   9027
name: Tim    ;    salary:   9000 ;  tax:  900 ; income:   8100
name: John   ;    salary:  12000 ;  tax: 1200 ; income:  10800
name: Lisa   ;    salary:  11000 ;  tax: 1100 ; income:   9900
要求像上面一样的对齐
tax 表示扣税金额和 income表示实际收入。注意扣税金额和 实际收入要取整数  
"""
# fo = open(r"E:\file1.txt",'r')
with open(r"E:\file1.txt",'r') as fo1, open(r"E:\file2.txt",'w') as fo2:
    alist = fo1.read().splitlines()
    # print(alist)
    for one in alist:
        a = one.split(";")
        name = a[0].split(":")[1]
        salary = int(a[1].split(":")[1].strip())*0.9
        tax = int(a[1].split(":")[1].strip())*0.1
        income = int(salary * 0.9)
        outPutStr = 'name: {:10} ; salary:{:6} ; tax: {:6} ;income: {:6}\n'.format(name, salary, tax, income)
        print(outPutStr)
        fo2.write(outPutStr)


