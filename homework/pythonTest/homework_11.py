#!/usr/bin/env python
# -*- coding: utf-8 -*-

__mtime__ = '2020-02-12'

from selenium import webdriver
from time import sleep

url = "http://music.baidu.com/top/new"
driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()
ele  = driver.find_element_by_css_selector(".top-list-item")
alist = ele.find_elements_by_tag_name("li")
for one in alist:
    attribute_name = one.find_element_by_css_selector(".status i").get_attribute('class')
    # print(attribute_name)
    if(attribute_name == 'up'):
        songg_title = one.find_element_by_css_selector(".song-title ").text
        songger = one.find_element_by_css_selector(".author_list").text
        print(f'{songg_title}:{songger}')
driver.quit()

