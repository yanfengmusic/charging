*** Settings ***
Library  SeleniumLibrary
Library  mylib

*** Test Cases ***
关键字测试
    ${num}  convert to integer  2020
    printargs  123
    printargs  ${num}
    ${list}  returnList
    printargs  ${list}   #把列表中的元素当做一个整体来传参
    printargs  @{list}   #把列表中的元素一个一个拎出来去传参
    printargs  @{list}[0]   #把列表中的元素一个一个拎出来去传参
    printargs  ${list[0]}   #把列表中的元素一个一个拎出来去传参
    ${dict}  returnDict
    printargs  ${dict}
    printargs  ${dict['key1']}  #使用python表达式的方式，就必须要加引号
    printargs  @{dict}
#    printargs  @{dict}[key1]  #不需要加引号
循环
    [Documentation]  新语法
    ${list}   create list  a  b  c  d
    FOR  ${i}  In  @{list}
        log to console  ${i}
        log to console  ----
    END
    log to console  循环出结果

#    for range
    FOR  ${one}  In RANGE  10
        log to console  ${one}
    END



