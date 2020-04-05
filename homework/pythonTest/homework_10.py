#!/usr/bin/env python
# -*- coding: utf-8 -*-

__mtime__ = '2020-02-09'
"""
1. 访问天气查询网站（网址如下），查询江苏省天气 
http://www.weather.com.cn/html/province/jiangsu.shtml
2. 获取江苏所有城市的天气，并找出其中每天最低气温最低的城市，显示出来，比如 
温度最低为12℃, 城市有连云港 盐城 

"""

from selenium import webdriver
from time import sleep
import requests
import re
import pprint
url = 'http://www.weather.com.cn/html/province/jiangsu.shtml'
driver = webdriver.Chrome() #本人将驱动放在了python解释器的安装的根目录，所以此处不需要填写驱动地址
driver.maximize_window()
driver.get(url)
def func1():
    ele = driver.find_element_by_id('forecastID')
    # print(ele.text)
    city_list = []
    lowest = 100
    # print(ele.text.split('\n'))
    for one in ele.text.split('℃\n'):
        one = one.replace('℃',"")
        # print(one.split('\n'))
        city_name = one.split('\n')[0]
        low = one.split('\n')[1][0]
        low = int(low)
        if low < lowest:
            lowest = low
            city_list.append(city_name)   #['南京', '无锡', '镇江', '南通', '扬州', '盐城', '连云港', '常州']
        elif low == lowest:
            city_list.append(city_name)
    print("温度最低时是%d℃,城市有:%s" %(lowest,";".join(city_list)))


def func2():
    city_list = driver.find_elements_by_css_selector("#forecastID > dl")
    # 定义城市字典
    city_dict = {}
    forNum = 0
    city_name = ""
    city_weather = ""
    for one in city_list:
        a = one.text
        if forNum%2 == 0:
            city_name = a
        else:
            city_weather = a
            city_dict[city_name] = city_weather.split("/")[0]
#            确保最低天是在列表中的第一位
        forNum += 1

#
#     city_list = []if int(city_dict[city_name][0].replace("℃","")) > int(city_dict[city_name][1].replace("℃","")) :
#             city_dict[city_name][0],city_dict[city_name][1] = city_dict[city_name][1],city_dict[city_name][0]
    city = []
    weather_num = 100
    for i in city_dict:
        if int(city_dict[i][0].replace("℃","")) <= weather_num:
            weather_num = int(city_dict[i][0].replace("℃",""))

            if len(city) == 0:
                city.append(i)
            elif len(city) == 1:
                city[0] = i
            else:
                city.clear()
                city.append(i)
    print("温度最低时，是%d℃,城市是%s" %(weather_num,"".join(city)))

if __name__ == '__main__':
    func1()
