#!/usr/bin/env python
# -*- coding: utf-8 -*-
import MySQLdb
import requests

__mtime__ = '2020-03-14'

def getCousersFromWeb():

    r = requests.get("http://localhost:90/api/mgr/sq_mgr/?action=list_course&pagenum=1&pagesize=20")
    # print(type(r.json()))
    # print(r.json()['retlist'])
    return (r.json()['retlist'])

def getCousersFromDB():
    # 打开数据库连接
    db = MySQLdb.connect(host="127.0.0.1", user="root", passwd="123456", port=3306, db="plesson",charset='utf8')
    # 获取操作游标
    cu = db.cursor()
    # 通过execute执行语句
    sql = "select * from sq_course"
    cu.execute(sql)
    data = cu.fetchall()
    # print(f"从数据库中查询到的课程信息{data}")
    cu.close()
    db.close()
    return data

if __name__ == '__main__':
    DBdata = getCousersFromDB()
    WebData = getCousersFromWeb()

    courseinfo = []
    # # print(WebData)
    def get():
        """将web端数据进行整理"""
        course = []
        for ele in WebData:
            courseinfo = []
            for key in ele:
                # print(ele[key])
                courseinfo.append(ele[key])
            course.append(courseinfo)

        return course

    course_web = get()
    # print(f"整理后从web端取出来的数据{course_web}")

    for ele in DBdata:
        course_db = list(ele)
        try:
            course_web.remove(course_db)
        except:
            False

    print(len(course_web))
    if len(course_web) == 0:
         print("数据是相同的")













