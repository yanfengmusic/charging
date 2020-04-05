#!/usr/bin/env python
# -*- coding: utf-8 -*-

__mtime__ = '2020-03-14'

import MySQLdb

db = MySQLdb.connect(host="127.0.0.1",user="root",password = "123456",port=3306,database="plesson",charset="utf8")
cursor = db.cursor()
try:
    # sql = "insert test values(2,'测试','aaa','2020-03-14')"
    #sql = "select * from test"
    # sql = "update test set runoob_title = 'title' where runoob_id = 1"
    sql = "delete from test where runoob_id = 1"
    cursor.execute(sql)
    n = cursor.rowcount  #影响的行数
    print(n)
    result = cursor.fetchall()
    # for row in result:
    #     print(row)
    print(result)
    db.commit()
except:
    db.rollback()
finally:
    cursor.close()
    db.close()
