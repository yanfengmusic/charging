*** Settings ***
Library  courseaction
Library  SeleniumLibrary
Library  Collections
*** Test Cases ***

case1
    [Setup]  deleteAllCourse
    [Teardown]  deleteAllCourse
#登录
    loginWebsite
#添加课程
    addCourse   robot1   robot框架   1
#判断课程是否被添加
    checkCourse   robot1
#关闭浏览器
    close browser

case2
    [Setup]     deleteAllCourse
    [Teardown]  deleteAllCourse
#登录
    loginWebsite
#添加课程
    addCourse     自动化测试   自动化测试   1
#判断课程是否被添加
    checkCourse    自动化测试
#关闭浏览器
    close browser

*** Keywords ***
loginWebsite
    open browser   http://localhost:90/mgr/login/login.html   chrome
    set selenium implicit wait  10
    input text  id=username      auto
    input text  id=password     sdfsdfsdf
    click element  css = .btn-success
addCourse
    [Arguments]  ${name}   ${desc}    ${idx}
    click element   css = [ng-click="showAddOne=true"]
    input text  css = [ng-model="addData.name"]             ${name}
    input text  css = [ng-model="addData.desc"]             ${desc}
    input text  css = [ng-model="addData.display_idx"]      ${idx}
    click element  css = [ng-click="addOne()"]
checkCourse  [Documentation]  判断元素
    [Arguments]  ${expect}
    sleep  2
    ${eles}      get webelements     css = tbody td:nth-child(2)
    ${courses}    evaluate  [ele.text for ele in $eles]
    should be true  $expect in $courses




