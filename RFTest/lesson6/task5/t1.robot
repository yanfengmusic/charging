#思路1：SeleniumLibrary
#思路2：python+selenium

*** Settings ***
Resource  rc.robot
Suite Setup  websetup
Suite Teardown  webteardown

*** Test Cases ***
case1
    [Setup]   deleteAllLesson
    [Teardown]  deleteAllLesson
    loginwebsite
    addCourse   robot    自动化框架课程    1
    #检查课程是否被添加
    checkCourse   robot

case2
    [Setup]   deleteAllLesson
    [Teardown]  deleteAllLesson
    loginwebsite
    addCourse   selenium    webui自动化    2
    #检查课程是否被添加
    checkCourse   selenium

