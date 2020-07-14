*** Settings ***
Library  SeleniumLibrary

*** Test Cases ***
#用例1
#    [Documentation]  测试用例1
#    import library  SeleniumLibrary
#    open browser  http://www.baidu.com    chrome
#    sleep  5
#    close browser
#    log to console   a
用例2
    ${a}   set variable  helloworld
    log to console   ${a}   #会输出到控制台
    log  ${a}               #会输出到日志中

