#!/usr/bin/env python
# -*- coding: utf-8 -*-

__mtime__ = '2020-02-18'

"""
打开 12306 网站  https://kyfw.12306.cn/otn/leftTicket/init
出发城市 填写 ‘南京南’， 到达城市 填写 ‘杭州东’ 
注意输入城市名前，一定要先点击一下输入框，否则查不到。 
而且输入城市名最后要包含一个回车符，否则输入框里面会自动清除
发车时间 选 06:00--12:00
发车日期选当前时间的下一天，也就是日期标签栏的，第二个标签
我们要查找的是所有 二等座还有票的车次，打印出这些有票的车次的信息（这里可以用xpath），结果如下：
G7641
G1505
G7393
G7689
"""

from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://kyfw.12306.cn/otn/leftTicket/init")
driver.maximize_window()
# 出发城市 填写 ‘南京南’， 到达城市 填写 ‘杭州东’
sleep(3)
from_city = driver.find_element_by_id("fromStationText")
from_city.click()
from_city.send_keys("南京南\n")

sleep(3)
to_city = driver.find_element_by_id("toStationText")
to_city.click()
to_city.send_keys("杭州东\n")
sleep(3)
# 发车时间 选 06:00--12:00
select = Select(driver.find_element_by_id("cc_start_time")).select_by_visible_text("06:00--12:00")

# 发车日期选当前时间的下一天，也就是日期标签栏的，第二个标签
sleep(3)
# driver.find_element_by_css_selector(".sel").click() #为什么这个.sel不行呢 这个class也是唯一的呢
driver.find_element_by_css_selector("#sear-sel li:nth-child(2)").click()

# 二等座还有票的车次，打印出这些有票的车次的信息
Trains = driver.find_elements_by_xpath(r".//*[@id='queryLeftTable']//td[4][@class]/../td[1]//a")
for one in Trains:
    print(one.text)


