*** Settings ***
Library  Collections          #RF操作列表和字典的一个库

*** Test Cases ***
case1
    ${list}   create list   1  2  3
    append to list  ${list}   a  b  c
    remove from list  ${list}  0
    log many  @{list}
    log many  ${list}

case2  [Documentation]  evaluate+python表达式
    ${list}   evaluate  [i for i in range(100)]
    log to console  ${list}
    ${list1}  evaluate  $list[:30]
    log to console   ${list1}
    ${dict}   evaluate  {"a":"qqqq","b":3}
    log to console  ${dict}
    ${var1}   evaluate  ${dict["a"]}
    log to console  ${var1}

case3
    ${list}   evaluate   [i for i in range(100)]
    log to console   ${list}
    ${list}   evaluate  $list[:30]
    ${dict}    evaluate  {"a":'hello',"b":3}
    ${var1}    evaluate  $dict.update({"a":"world"})
    #eval函数不能执行赋值操作  $dict["a"]=123  执行不了
    log to console  ${var1}
    log to console  ${dict["a"]}
    log to console  ${list}


