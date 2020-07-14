*** Settings ***
Suite Setup  log to console   套件级别初始化
Suite Teardown   log to console    套件级别清除
Test Setup   log to console   默认级别初始化
Test Teardown   log to console  默认级别清除



*** Test Cases ***
case1  [Documentation]  用例级别的setupTearDown  可以只有setup或者只有teardown  不是一定要成对出现
    [Setup]  log to console  用例执行初始化
#    [Setup]  fail  执行初始化     #如果setup失败 用例主体不会执行
    [Teardown]  log to console  用例执行清除动作    #任何情况下teardown都会执行，即使用例主体出错
    log to console  执行主体
#    should be true  1>2


