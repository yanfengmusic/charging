#!/usr/bin/env python
# -*- coding: utf-8 -*-


__mtime__ = '2020-02-15'

"""
登录 51job ，
http://www.51job.com

输入搜索关键词 "python"， 地区选择 "杭州"（注意，如果所在地已经选中其他地区，要去掉）， 
搜索最新发布的职位， 抓取页面信息。 得到如下的格式化信息

Python开发工程师 | 杭州纳帕科技有限公司 | 杭州 | 0.8-1.6万/月 | 04-27
Python高级开发工程师 | 中浙信科技咨询有限公司 | 杭州 | 1-1.5万/月 | 04-27
高级Python开发工程师 | 杭州新思维计算机有限公司 | 杭州-西湖区 | 1-1.5万/月 | 04-27

"""
from selenium import webdriver
from time import sleep


driver = webdriver.Chrome()
driver.get("http://www.51job.com")
driver.maximize_window()
driver.implicitly_wait(20)
# 查找搜索框,并输入python
# sleep(3)
driver.find_element_by_css_selector("#kwdselectid").send_keys("python")
# sleep(3)
# 点击城市输入框，选择城市
driver.find_element_by_css_selector("#work_position_input").click()
# 找到已经选择的城市，进行删除
city_area = driver.find_element_by_css_selector("#work_position_click_multiple_selected")
# sleep(5)
city_list = city_area.find_elements_by_css_selector(".ttag")
if city_list:
    for one in city_list:
        one.click()

# 找到杭州并点击选中
driver.find_element_by_css_selector("#work_position_click_center_right_list_category_000000_080200").click()
driver.find_element_by_css_selector("#work_position_click_bottom_save").click()

sleep(5)
# 回到搜索框进行搜索
driver.find_element_by_css_selector(".ush> button").click()   #???????????????

# 搜索结果中查找公司薪资等详细信息
info_ele = driver.find_elements_by_css_selector("#resultList div[class='el']")
for i in info_ele:
    # print(i.text)
    ele_list = i.text.split("\n")
    # print(ele_list)
    print("|".join(ele_list))

driver.quit()







