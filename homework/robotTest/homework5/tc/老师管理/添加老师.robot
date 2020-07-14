*** Settings ***
Library    Collections
Library    pylib.WebOpAdmin

*** Test Cases ***
添加老师1
#    [Setup]  run keywords   setupWebTest  10   1   chrome
    [Setup]  run keywords   loginWebsite
    ...      AND   deleteAllCourse
    ...      AND   deleteAllTeacher
    addCourse   初中语文    语文课     2
    addCourse   初中数学    数学课     1

    addTeacher     刘德华   liudehua    偶像    1   初中语文
    ${teachers}    GetTeacherList
    should be true  $teachers==[u'刘德华']
    [Teardown]      run keywords    deleteAllTeacher
    ...      AND   deleteAllCourse














