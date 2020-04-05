#!/usr/bin/env python
# -*- coding: utf-8 -*-

__mtime__ = '2020-02-16'

"""
登录 http://www.51job.com
    点击高级搜索
    输入搜索关键词 python 
    地区选择 杭州
    职能类别 选 计算机软件 -> 高级软件工程师
    公司性质选 外资 欧美
    工作年限选 1-3 年
搜索最新发布的职位， 抓取页面信息。 得到如下的格式化信息
    Python开发工程师 | 杭州纳帕科技有限公司 | 杭州 | 0.8-1.6万/月 | 04-27
    Python高级开发工程师 | 中浙信科技咨询有限公司 | 杭州 | 1-1.5万/月 | 04-27
"""

from selenium import webdriver
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.implicitly_wait(50)
driver.get("http://www.51job.com")
# driver.maximize_window()
# 点击搜索
driver.find_element_by_css_selector(".more").click()
# 输入python关键字
driver.find_element_by_css_selector("#kwdselectid").send_keys("python")
# 点击选择地区进入到选择页面
driver.find_element_by_css_selector("#work_position_input").click()

# 清空已经存在的地区
# city_areas = WebDriverWait(driver,timeout=10).until(lambda x: x.find_element("id",'#work_position_click_multiple_selected'))
sleep(5)
city_areas = driver.find_element_by_css_selector('#work_position_click_multiple_selected')
city_list = city_areas.find_elements_by_css_selector(".ttag") #????????????????
if city_list:
    for one in city_list:
        print(one.text)
        one.click()

# 选中杭州
driver.find_element_by_css_selector("#work_position_click_center_right_list_category_000000_080200").click()
driver.find_element_by_css_selector("#work_position_click_bottom_save").click()

driver.find_element_by_css_selector("#historylist>.rtit ").click()

# 职能类别选计算机软件 -> 高级软件工程师
driver.find_element_by_css_selector("#funtype_click").click()
driver.find_element_by_css_selector("#funtype_click_center_right_list_category_0100_0100").click()
driver.find_element_by_css_selector("#funtype_click_center_right_list_sub_category_each_0100_0106").click()
driver.find_element_by_css_selector("#funtype_click_bottom_save").click()

# 公司性质选外资欧美
driver.find_element_by_css_selector("#cottype_list").click()
driver.find_element_by_css_selector('.ul span[title="国企"]').click()

# 工作年限选1 - 3年
driver.find_element_by_css_selector("#workyear_list").click()
driver.find_element_by_css_selector('.ul span[title="1-3年"]').click()


# 保存并搜索
driver.find_element_by_css_selector(".btnbox.p_sou>span").click()

# 搜索结果中查找公司薪资等详细信息
info_ele = driver.find_elements_by_css_selector("#resultList div[class='el']")
for i in info_ele:
    # print(i.text)
    ele_list = i.text.split("\n")
    # print(ele_list)
    print("|".join(ele_list))

driver.quit()



