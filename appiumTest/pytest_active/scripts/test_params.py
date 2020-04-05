#!/usr/bin/env python
# -*- coding: utf-8 -*-

__mtime__ = '2020-03-06'

from appium import webdriver
import pytest

class TestLogin:

    # def setup(self):
    #
    #     # server 启动参数
    #     desired_caps = {}
    #     # 设备信息
    #     desired_caps['platformName'] = 'Android'
    #     desired_caps['platformVersion'] = '5.1'
    #     desired_caps['deviceName'] = '192.168.164.101:5555'
    #     # app信息
    #     desired_caps['appPackage'] = 'com.android.settings'
    #     desired_caps['appActivity'] = '.Settings'
    #     # 中文
    #     desired_caps['unicodeKeyboard'] = True
    #     desired_caps['resetKeyboard'] = True
    #     # 声明对象
    #     self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    @pytest.mark.parametrize("keys", ["1", "2"])
    def test_search(self, keys):
        # 点击放大镜
        self.driver.find_element_by_id("com.android.settings:id/search").click()
        # 输入文本框的文字 "1"
        self.driver.find_element_by_id("android:id/search_src_text").send_keys(keys)


    @pytest.mark.parametrize(("username", "password"), [("zhangsan", "123"), ("lisi", "456")])
    def test_search(self, username, password):
        print(username)
        print(password)
        print("-----")



        # # 点击放大镜
        # self.driver.find_element_by_id("com.android.settings:id/search").click()
        # # 输入文本框的文字 "1"
        # self.driver.find_element_by_id("android:id/search_src_text").send_keys(keys)

    # def login(self):
    #     print("haha")


