*** Settings ***
Library    pylib.Web

*** Test Cases ***
添加课程1
    [Setup]  run keywords   loginWebsite
    ...      AND   deleteAllCourse
    ...      AND   deleteAllTeacher
    addCourse   初中语文    语文课     2
    [Teardown]      run keywords    deleteAllCourse











