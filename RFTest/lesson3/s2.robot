*** Settings ***
Library  Collections
Suite Setup   log to console      套件刚刚开启时，清除部分用例数据
Suite Teardown   log to console      套件最后结束时执行的部分
*** Test Cases ***
测试1
    [Documentation]  测试用例级别的清除
    [Setup]  log to console      用例执行前，清除部分用例数据
    [Teardown]  log to console   用例执行完之后再清除
    ${var} =   create list   hello   world
    append to list  ${var}  a  b  c
    log to console  ${var}
    fail

#自动化测试用例设计规范
#1/用例之间不可存在耦合性
#2/用例执行完成必须清除自身产生的测试数据,放置被其他用例造成干扰,保证测试环境整洁
