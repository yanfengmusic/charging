#!/usr/bin/env python
# -*- coding: utf-8 -*-

__mtime__ = '2020-03-14'

import unittest
import MySQLdb

class Delete(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """连接数据库"""
        cls.db = MySQLdb.connect("127.0.0.1","root","123456","plesson",3306)
        return cls.db
    def test_1(self):
        self.assertTrue(12)

    @classmethod
    def tearDownClass(cls):
        """"""
        try:
            cursor = cls.db.cursor()
            sql = "delete from test where runoob_id = 1"
            cursor.execute(sql)
            cls.db.commit()
            print("删除成功")
            num = cursor.rowcount
            print(num)
        except Exception as info:
            print(info)
            cls.db.rollback()
        finally:
            cursor.close()
            cls.db.close()




