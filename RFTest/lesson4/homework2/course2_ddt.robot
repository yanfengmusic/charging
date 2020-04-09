*** Settings ***
Library  courseaction
Library  SeleniumLibrary
Library  Collections
Resource  ../rc.robot
*** Test Cases ***

case2
    [Setup]     deleteAllCourse
    [Teardown]  deleteAllCourse
    [Template]  loginandcheck
    robot      自动化测试框架      1
    selenium    webui测试         2
    jmeter      接口测试          3

*** Keywords ***
loginandcheck
    [Arguments]  ${name}   ${desc}    ${idx}
    #登录
    loginWebsite
#添加课程
    addCourse     ${name}   ${desc}   ${idx}
#判断课程是否被添加
    checkCourse    ${name}
#关闭浏览器
    close browser




