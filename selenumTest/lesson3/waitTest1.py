#!/usr/bin/env python
# -*- coding: utf-8 -*-

__mtime__ = '2020-02-12'
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")


# driver.implicitly_wait(5) #隐式等待时间 全局通用


driver.find_element_by_css_selector("#kw").send_keys("松勤\n")


driver.find_element_by_css_selector(r'#\34  > h3 > a > em').click()
