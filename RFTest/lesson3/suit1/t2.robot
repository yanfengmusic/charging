
*** Test Cases ***
case1  [Documentation]  用例级别的setupTearDown  可以只有setup或者只有teardown  不是一定要成对出现
    [Setup]  log to console  用例初始化
#    [Setup]  fail  执行初始化     #如果setup失败 用例主体不会执行
    log to console  用例清除动作    #任何情况下teardown都会执行，即使用例主体出错
    log to console  执行主体
#    should be true  1>2


