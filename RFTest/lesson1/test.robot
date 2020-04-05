*** Settings ***
Library  SeleniumLibrary


*** Test Cases ***
用例1
#用例主体部分另起一行，并且至少缩进两个空格
#关键字和参数至少空两格，如果传多个参数，参数与参数之期间也至少空两格
  log to console    hello robot
用例2
   log to console  测试用例2
用例3
#    百度搜索小米
    [Documentation]
    Open Browser                https://www.baidu.com   chrome
    set selenium implicit wait   1
    input text                  id=kw                   松勤\n
    ${res}                       get text               id=1
    should contain               ${res}                 松勤网
    close browser



