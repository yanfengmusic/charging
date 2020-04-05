#!/usr/bin/env python
# -*- coding: utf-8 -*-

__mtime__ = '2020-01-14'

# def getSum():
#     print("test")
# import sys
# import pprint
# # print(sys.path)
#
# pprint.pprint(sys.path)
#
# from selenium import webdriver
# from time import sleep
# # driver = webdriver.Chrome()
# driver = webdriver.Firefox()
# driver.get("http://www.baidu.com")
# sleep(5)
# driver.close()
def func():
    print("step1")
    print("step2")
    print("step3")


fileDir = r"E:/0005_1.txt"
def putInToDict(fileName):
    resDict = {}
    with open(fileName) as fo:
        lines = fo.read().splitlines()
        pass
        for line in lines:
            line = line.replace("\t","").replace("(","").replace(")","").replace("'","").replace(";","")
            temp = line.split(",")
            checkTime = temp[0].strip()
            lessId = int(temp[1].strip())
            userId = int(temp[2].strip())
            func()

            info = {"lessId":lessId,"checkTime":checkTime}
            if userId not in resDict:
                resDict[userId] = [info]
            else:
                resDict[userId].append(info)
    return resDict


import pprint
pprint.pprint(putInToDict(fileDir))




#!/usr/bin/env python
# -*- coding: utf-8 -*-



import requests
web_url = "https://search.51job.com/list/230200,000000,0000,00,9,99,%25E8%2587%25AA%25E5%258A%25A8%25E5%258C%2596%25E6%25B5%258B%25E8%25AF%2595%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="
resp = requests.get(web_url)
resp.encoding = 'gbk'
print(resp.text) #返回是字符串
# print(resp.content)#返回是byte
# print(resp.request.headers)#请求头
# print(resp.headers) #响应头
# print(resp.request.body)#请求体

# 提取有用的数据
"""
<div class="el">
        <p class="t1 ">
            <em class="check" name="delivery_em" onclick="checkboxClick(this)"></em>
            <input class="checkbox" type="checkbox" name="delivery_jobid" value="115042441" jt="0" style="display:none">
            <span>
                <a target="_blank" title="自动化测试工程师" href="https://jobs.51job.com/beijing-cyq/115042441.html?s=01&amp;t=0" onmousedown="">
                    自动化测试工程师                </a>
            </span>
                                                                    </p>
        <span class="t2"><a target="_blank" title="北京友聚四海网络科技有限公司" href="https://jobs.51job.com/all/co5558174.html">北京友聚四海网络科技有限公司</a></span>
        <span class="t3">北京-朝阳区</span>
        <span class="t4">1-1.5万/月</span>
        <span class="t5">02-04</span>
    </div>

"""
import re
# re.findall("<div class="el">",)






import xlwt
# 创建一个Excel表文件
workBook = xlwt.Workbook(encoding='utf-8')
# 在文件对象中再创建一个sheet
work_Sheet = workBook.add_sheet("51job.res")
colName = ['职位名','公司名','工作地点','薪资','发布时间']
for col in range(0,len(colName)):
    work_Sheet.write(0,col,colName[col])
# workBook.save('e:\\51job.xls')#存放到具体的磁盘路径

