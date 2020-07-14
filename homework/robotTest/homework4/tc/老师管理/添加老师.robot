*** Settings ***
Resource  rflib/rc.robot

Suite Setup      websetup
Suite Teardown   webtearown

*** Test Cases ***
添加老师1
    [Setup]  run keywords   deleteAllTeacher  AND   deleteAllCourse
    ...      AND  addCourse    初中语文    语文课    2
    ...      AND  addCourse    初中数学    数学课    1

    addTeacher    刘德华   liudehua    偶像    1   初中语文
    checkTecher   刘德华
    [Teardown]  run keywords   deleteAllTeacher  AND   deleteAllCourse














