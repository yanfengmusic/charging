*** Settings ***
Library  courseaction

*** Test Cases ***

case1
    [Setup]  deleteAllCourse
    open browser   http://localhost:90/mgr/login/login.html
    set selenium implicit wait  10
    input text  id=uesername
    input text  id=password
    click element  css = .btn-success
#    开始添加课程
    click element

