#!/usr/bin/env python
# -*- coding: utf-8 -*-

__mtime__ = '2020-03-14'

import MySQLdb

# 打开数据库连接
db = MySQLdb.connect(host="127.0.0.1",user="root",passwd="123456",port=3306,db="plesson")
# 获取操作游标
cursor = db.cursor()
# 通过execute执行语句
# cursor.execute("select version();")
sql = """CREATE TABLE IF NOT EXISTS `test1`(
   `runoob_id` INT UNSIGNED AUTO_INCREMENT,
   `runoob_title` VARCHAR(100) NOT NULL,
   `runoob_author` VARCHAR(40) NOT NULL,
   `submission_date` DATE,
   PRIMARY KEY ( `runoob_id` )
)ENGINE=InnoDB DEFAULT CHARSET=utf8;
"""
cursor.execute(sql)
data = cursor.fetchone()
data = cursor.fetchall()
# data = cursor.fetchmany(x)
print("数据库版本是",data)


# 释放资源
cursor.close()
db.close()
