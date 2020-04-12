*** Settings ***
#导入类  模块名.类名
Library  tlib2.SubLibrary
#导入的这个类存在初始化方法的 需要在导入后就将初始化的参数传入
Library  tlib2.SubLibrary2      localhost    8080
#、如果class和模块的名字同名，则可以不写

*** Test Cases ***
test1
    ${var}    returnint
    log to console  ${var}
test2
    ${v}    printaddr
