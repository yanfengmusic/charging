#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__:hp

__mtime__ = '2020-03-22'

import paramiko
import pprint

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("192.168.64.132",22,"root","root")
stdin,stdout,stuerr = ssh.exec_command("ls")
# print(stdout)
pprint.pprint(stdout.read().decode("utf8"))

sftp = ssh.open_sftp()
# 将本地文件传送到远程机器
# sftp.put("源文件路径","远程机目标路径")
# 从远程机下载文件
sftp.get("远程机路径","本地路径")


# 释放资源
ssh.close()
