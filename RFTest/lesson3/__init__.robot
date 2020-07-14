*** Settings ***
#套件目录文件的初始化配置的名称，__init__.robot 不能写错，写错了，运行时不会报错，因为他不知道 你是套件的setupteardown还是普通的robot文件
Suite Setup      log to console   \n --- Suite lesson3 Setup ---
Suite Teardown   log to console   \n --- Suite lesson3 Teardown ---
