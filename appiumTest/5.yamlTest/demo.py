#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__:hp

__mtime__ = '2020-03-18'
import yaml

def main():
    with open("./data.yaml","r")as file:
        data = yaml.load(file)
        print(data)

if __name__ == '__main__':
    main()

