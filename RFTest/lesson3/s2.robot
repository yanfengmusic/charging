*** Settings ***
Library  Collections
Suite Setup      log to console     套件执行
Suite Teardown   log to console     套件结束
Test Setup      log to console     testsetup
Test Teardown   log to console     Teardown
*** Test Cases ***
测试1
    [Documentation]  测试用例级别的清除
    [Setup]  log to console      用例执行前，清除部分用例数据
    ${var} =   create list   hello   world
    append to list  ${var}  a  b  c
    log to console  ${var}
#    fail
    [Teardown]  log to console   用例执行完之后再清除

#自动化测试用例设计规范
#1/用例之间不可存在耦合性
#2/用例执行完成必须清除自身产生的测试数据,放置被其他用例造成干扰,保证测试环境整洁
测试2
    log to console  测试用例2
测试3
    log to console  测试用例3

#指定目录级别的套件:这样就会执行目录级别的套件
robot -s st1 suit1
#指定某条测试用例
robot -t 测试1 suit1

