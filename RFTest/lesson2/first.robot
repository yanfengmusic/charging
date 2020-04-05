*** Settings ***
Library  SeleniumLibrary
Library  mylib    #导包后，应用时，会提示找不到这个模块，首先可以在cmd中 set pythonpath = . 的方式来设置临时变量，关闭后会自动失效；还有一种方式：在执行的时候robot --pythonpath . first.robot  可以简写为robot -P . first.robot


*** Test Cases ***
#import library  SeleniumLibrary
用例1
     [Documentation]  验证Unicode字符串
     checkScore  ${99}  #花括号会按照python表达式的语法去解析这个变量
用例2
    [Documentation]  检查点 类型的关键字 一旦执行失败 后面就不执行了
    should end with  hello  o
    should be equal  hello  hello
#    should be equal  65  ${65}
     should be equal as strings   65  ${65}
#    should be true  <condition>  参数为表达式
     should be true  65>64

用例3
     ${hello}   set variable  hello
     should be true  "hello" == "${hello}"   #使用${hello}来传递变量时，会默认将字符串的''的符号去掉
     should be true  'hello' == $hello   #如果python表达式，可以用$加变量名，来保证原来变量的类型符号



