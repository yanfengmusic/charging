#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__:hp

__mtime__ = '2020-04-01'
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
"""
陈旧的元素引用:元素没有附加到页面文档
查找元素是引用过期，页面刷新后，之前查找到的元素被更新了，导致元素不能正常使用
selenium.common.exceptions.StaleElementReferenceException: Message: stale element reference: element is not attached to the page document
  (Session info: chrome=80.0.3987.122)

"""
class Web():
    # 保证仅实例化一次
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.timeout = 10
        self.t = 1
        self.driver.implicitly_wait(10)

    # def setupWebTest(self,time,t,driverType='chrome'):
    #     self.timeout=time
    #     self.t = t
    #     self.diver=None
    #     if driverType == 'chrome':
    #         self.driver= webdriver.Chrome()
    #     elif  driverType == 'firefox':
    #         self.driver = webdriver.Firefox()
    #     else:
    #         raise Exception('unknow driver type %s' % driverType)
    #     self.driver.implicitly_wait(10)
        # return self.driver



    def loginWebsite(self):
        self.driver.get("http://localhost:90/mgr/login/login.html")
        self.driver.implicitly_wait(10)
        # self.driver.maximize_window()
        self.driver.find_element_by_id("username").clear()
        self.driver.find_element_by_id("username").send_keys("auto")
        self.driver.find_element_by_id("password").clear()
        self.driver.find_element_by_id("password").send_keys("sdfsdfsdf")
        self.driver.find_element_by_class_name("btn.btn-success").click()

    def deleteAllCourse(self):
        self.driver.implicitly_wait(10)
        """
        删除所有
        :return:
        """

        self.driver.find_element_by_css_selector('[ui-sref="course"]').click()
        self.driver.implicitly_wait(5)
        # ele_teahcer = WebDriverWait(self.driver,self.timeout,self.t).until(lambda x : x.find_element(*locator))
        # ele_teahcer.click()
        while True:
            delete_buttons = self.driver.find_elements_by_css_selector('[ng-click="delOne(one)"]')
        # while True:
            print(len(delete_buttons))
            if delete_buttons == []:
                print("删除完毕")
                break
                sleep(2)
            delete_buttons[0].click()
            sleep(2)
            self.driver.find_element_by_class_name("btn.btn-primary").click()
            # driver.find_element_by_class_name("btn.btn-primary").send_keys()
            sleep(2)

        # driver.quit()


    def deleteAllTeacher(self):
        self.driver.implicitly_wait(10)
        """
        删除所有
        :return:
        """

        self.driver.find_element_by_css_selector('[ui-sref="teacher"]').click()
        self.driver.implicitly_wait(5)
        # ele_teahcer = WebDriverWait(self.driver,self.timeout,self.t).until(lambda x : x.find_element(*locator))
        # ele_teahcer.click()
        while True:
            delete_buttons = self.driver.find_elements_by_css_selector('[ng-click="delOne(one)"]')
        # while True:
            print(len(delete_buttons))
            if delete_buttons == []:
                print("删除完毕")
                break
                sleep(2)
            delete_buttons[0].click()
            sleep(2)
            self.driver.find_element_by_class_name("btn.btn-primary").click()
            # driver.find_element_by_class_name("btn.btn-primary").send_keys()
            sleep(2)

        # driver.quit()

    def addCourse(self,courseName,desc,idx):
        """添加课程"""
        courseName = str(courseName)
        desc = str(desc)
        idx = str(idx)
        self.driver.implicitly_wait(10)
        loc_addButton = ('css selector','.btn-blue')
        loc_courseName = ('css selector','[ng-model="addData.name"]')
        loc_courseDesc = ('css selector','[ng-model="addData.desc"]')
        loc_idx = ('css selector','[ng-model="addData.display_idx"]')
        loc_creatButton = ('css selector','[ng-click="addOne()"]')

        self.driver.find_element_by_css_selector('[ui-sref="course"]').click()
        ele_addButton = WebDriverWait(self.driver,self.timeout,self.t).until(lambda x : x.find_element(*loc_addButton))
        ele_addButton.click()
        sleep(3)
        ele_courseName = WebDriverWait(self.driver, self.timeout, self.t).until(lambda x: x.find_element(*loc_courseName))
        ele_courseDesc = WebDriverWait(self.driver, self.timeout, self.t).until(lambda x: x.find_element(*loc_courseDesc))
        ele_idx = WebDriverWait(self.driver, self.timeout, self.t).until(lambda x: x.find_element(*loc_idx))
        ele_creatButton = WebDriverWait(self.driver, self.timeout, self.t).until(lambda x: x.find_element(*loc_creatButton))
        ele_courseName.send_keys(courseName)
        ele_courseDesc.send_keys(desc)
        ele_idx.send_keys(idx)
        ele_creatButton.click()
        sleep(3)



    # def AddCourse(self, name,desc,idx):
    #     self.driver.find_element_by_css_selector('ul.nav a[ui-sref=course]').click()
    #
    #     self.driver.find_element_by_css_selector('button[ng-click^=showAddOne]').click()
    #
    #     ele = self.driver.find_element_by_css_selector("input[ng-model='addData.name']")
    #     ele.clear()
    #     ele.send_keys(name)
    #
    #     ele = self.driver.find_element_by_tag_name("textarea")
    #     ele.clear()
    #     ele.send_keys(desc)
    #
    #     ele = self.driver.find_element_by_css_selector("input[ng-model='addData.display_idx']")
    #     ele.clear()
    #     ele.send_keys(idx)
    #
    #     self.driver.find_element_by_css_selector('button[ng-click^=addOne]').click()
    #
    #     sleep(1)


    def addTeacher(self,realname,loginName,desc,idx,coueseName):
        """添加老师"""
        self.driver.implicitly_wait(10)
        loc_teacher = ('css selector','[ui-sref="teacher"]')
        loc_addButton = ('css selector','.btn-blue')
        loc_RealName = ('css selector','[ng-model="addEditData.realname"]')
        loc_loginName = ('css selector','[ng-model="addEditData.username"]')
        loc_desc = ('css selector','[ng-model="addEditData.desc"]')
        loc_idx = ('css selector','[ng-model="addEditData.display_idx"]')
        loc_courseSelect = ('css selector','[ng-model="$parent.courseSelected"]')
        loc_addMark = ('class name','fa')
        loc_confirmButton = ('css selector','[ng-click="addOne()"]')

        WebDriverWait(self.driver, self.timeout, self.t).until(lambda x : x.find_element(*loc_teacher)).click()
        # ele_teacher.click()
        sleep(2)
        WebDriverWait(self.driver, self.timeout, self.t).until(lambda x: x.find_element(*loc_addButton)).click()
        # ele_addButton.click()
        WebDriverWait(self.driver, self.timeout, self.t).until(lambda x: x.find_element(*loc_RealName)).send_keys(realname)
        WebDriverWait(self.driver, self.timeout, self.t).until(lambda x: x.find_element(*loc_loginName)).send_keys(loginName)
        WebDriverWait(self.driver, self.timeout, self.t).until(lambda x: x.find_element(*loc_desc)).send_keys(desc)
        WebDriverWait(self.driver, self.timeout, self.t).until(lambda x: x.find_element(*loc_idx)).send_keys(idx)
        ele_courseSelect = WebDriverWait(self.driver, self.timeout, self.t).until(lambda x: x.find_element(*loc_courseSelect))
        ele_addMark = WebDriverWait(self.driver, self.timeout, self.t).until(lambda x: x.find_element(*loc_addMark))
        ele_confirmButton = WebDriverWait(self.driver, self.timeout, self.t).until(lambda x: x.find_element(*loc_confirmButton))

        select = Select(ele_courseSelect)
        select.select_by_visible_text(coueseName)
        ele_addMark.click()
        ele_confirmButton.click()

        sleep(3)

    # def  AddTeacher(self,realname,username,desc,idx,lesson):
    #     self.driver.find_element_by_css_selector('ul.nav a[ui-sref=teacher]').click()
    #
    #     self.driver.find_element_by_css_selector('button[ng-click^=showAddOne]').click()
    #
    #     ele = self.driver.find_element_by_css_selector(
    #         "input[ng-model='addEditData.realname']")
    #     ele.clear()
    #     ele.send_keys(realname)
    #
    #     ele = self.driver.find_element_by_css_selector(
    #         "input[ng-model='addEditData.username']")
    #     ele.clear()
    #     ele.send_keys(username)
    #
    #     ele = self.driver.find_element_by_css_selector(
    #         "textarea[ng-model='addEditData.desc']")
    #     ele.clear()
    #     ele.send_keys(desc)
    #
    #     ele = self.driver.find_element_by_css_selector(
    #         "input[ng-model='addEditData.display_idx']")
    #     ele.clear()
    #     ele.send_keys(idx)
    #
    #     select = Select(self.driver.find_element_by_css_selector(
    #         'select[ng-model*=courseSelected]'))
    #     select.select_by_visible_text(lesson)
    #
    #     self.driver.find_element_by_css_selector('button[ng-click*=addTeachCourse]').click()
    #
    #     self.driver.find_element_by_css_selector('button[ng-click^=addOne]').click()
    #
    #     sleep(1)
    def addTrainClass(self,trainClassName,trainCourseDesc,idx,coueseName):
        """添加培训班"""
        self.driver.implicitly_wait(10)
        loc_trainClass = ('css selector','[ui-sref="training"]')
        loc_trainClassButton = ('css selector','.btn-blue')
        loc_trainClassName = ('css selector', '[ng-model="addEditData.name"]')
        loc_trainCourseDesc = ('css selector', '[ng-model="addEditData.desc"]')
        loc_idx = ('css selector', '[ng-model="addEditData.display_idx"]')
        loc_courseSelect = ('css selector', '[ng-model="$parent.courseSelected"]')
        loc_addMark = ('class name', 'fa')
        loc_confirmButton = ('css selector', '[ng-click="addOne()"]')

        ele_trainClass = WebDriverWait(self.driver,self.timeout,self.t).until(lambda x : x.find_element(*loc_trainClass))
        ele_trainClass.click()

        ele_trainClassButton = WebDriverWait(self.driver, self.timeout, self.t).until(lambda x: x.find_element(*loc_trainClassButton))
        ele_trainClassButton.click()
        sleep(2)
        ele_trainClassName = WebDriverWait(self.driver, self.timeout, self.t).until(lambda x: x.find_element(*loc_trainClassName))
        ele_trainCourseDesc = WebDriverWait(self.driver, self.timeout, self.t).until(lambda x: x.find_element(*loc_trainCourseDesc))
        ele_idx = WebDriverWait(self.driver, self.timeout, self.t).until(lambda x: x.find_element(*loc_idx))
        ele_courseSelect = WebDriverWait(self.driver, self.timeout, self.t).until(lambda x: x.find_element(*loc_courseSelect))
        ele_addMark = WebDriverWait(self.driver, self.timeout, self.t).until(lambda x: x.find_element(*loc_addMark))
        ele_confirmButton = WebDriverWait(self.driver, self.timeout, self.t).until(lambda x: x.find_element(*loc_confirmButton))

        ele_trainClassName.send_keys(trainClassName)
        ele_trainCourseDesc.send_keys(trainCourseDesc)
        ele_idx.send_keys(idx)
        select = Select(ele_courseSelect)
        select.select_by_visible_text(coueseName)
        ele_addMark.click()
        ele_confirmButton.click()
        sleep(3)

    def  GetTeacherList(self):
        self.driver.find_element_by_css_selector('ul.nav a[ui-sref=teacher]').click()
        # 试试 //tr/td[2]/span/text()
        eles = self.driver.find_elements_by_css_selector('tr>td:nth-child(2)')

        return  [ele.text for ele in eles]


    def GetCourseList(self):
        self.driver.find_element_by_css_selector('ul.nav a[ui-sref=course]').click()
        # 试试 //tr/td[2]/span/text()
        eles = self.driver.find_elements_by_css_selector('tr>td:nth-child(2)')

        return  [ele.text for ele in eles]

    def GetTrainClassList(self):
        self.driver.find_element_by_css_selector('[ui-sref="training"]').click()
        # 试试 //tr/td[2]/span/text()
        eles = self.driver.find_elements_by_css_selector('tr>td:nth-child(2)')

        return [ele.text for ele in eles]

    def closeBrower(self):
        self.driver.quit()




if __name__ == '__main__':
    loc_teacher = ('css selector', '[ui-sref="teacher"]')
    loc_course = ('css selector','[ui-sref="course"]')
    loc_trainClass = ('css selector','[ui-sref="training"]')
    driver = webdriver.Chrome()
    woa = Web()
    # woa.setupWebTest()
    woa.loginWebsite()

    woa.deleteAllCourse()
    woa.deleteAllTeacher()
    # woa.deleteAll("trainClass")

    woa.addCourse("初中语文","语文课程","1")
    woa.addTeacher("刘德华","andylau","一代人的心情",1,"初中语文")
    # woa.addTrainClass("培训一班","培训一班",1,"初中语文")

    # print(woa.GetTrainClassList())
    print(woa.GetCourseList())
    print(woa.GetTeacherList())

    woa.closeBrower()

