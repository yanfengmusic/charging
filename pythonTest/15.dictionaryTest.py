#!/usr/bin/env python
# -*- coding: utf-8 -*-

__mtime__ = '2020-01-11'

"""
字典的定义与特性：
1、键：
    1.可以是：int,str,tuple，float不可以改变的类型
    2.不可以是：列表、字典等，可以改变的值的，也就是我们之前说的hash类型包括list
    3.最常用的是字符串的类型
2、值：任意类型
3、dictionary是可以改变的
4、key是唯一的
5、无序的

"""

dict1 = {'name':'lili','age':15}
print(type(dict1))
print(dict1['name'])#根据键来查询，如果键名不存在，会报错

students = {

        'mike':{'age':15,
                'height':180,
                'weight':80,
                },
        'tom':{
                'age':18,
                'height':80,
                'weight':100,
              }

    }

print(students['tom']['age'])#字典里面套用字典，以后UI自动化用的不多，但是在接口自动化里面经常使用

"""
常用操作：
1.查询：print(dict1['name']) 根据键来查询，如果键名不存在，会报错
2.修改：dict1['name'] = 'jack'
3.增加: dict1['weight'] = 150 从python3开始，默认从尾部开始增加，python2是随机的
4.通过in去判断，键存不存在
5.删除:del['key'];dict1.pop['name']也是有返回值的，没有remove方法
6.len(dict1):指的是键的个数，也是值的个数
7.清空：dict1.clear()清空，地址还在，只不过值不存在了
8.dict1 = {} 重新赋值
9.获取所有的键：dict1.keys() 返回值类型是键类型,是类列表，不支持下标，支持for循环
10.获取所有的值：dict1.values()返回值类型是类列表，不支持下标，支持for循环
11.获取所有的键、值：dict1.items()
12.字典的合并：dict1.update(字典/键值对),合并完成后变成一个新的字典
13.字典的遍历
"""

dict1['weight'] = 150
# print(dict1)

# def func():
#     # dict1.clear()
#     dict1={}
#     print(dict1)
# func()
# print(dict1)


print(dict1.keys()) #返回值类型是类列表
# for one in dict1.keys():
#     print(one)
# 可以通过list()强制转换
print(list(dict1.keys()))

for one in dict1.items():#一个one，取的是一个键值对的元祖
# for one,a in dict1.items():#两个变量时，是取一个键，一个值
    print(one)

d = {1:'1',2:'2'}
d.update({4:'4',5:'5'})
d.update(dict1)
print(d)

"""
字典的遍历：
    1.对字典的遍历，遍历出来的是键
    2.对items进行遍历，简历出来的是键值对
"""
for one in students:
    pass
for one in students.items():
    pass

"""
字典的使用：
1.一些简单的是数据，无需字典，列表就可以了
2.字典是无序的，如果需要顺序，则不能用字典

"""
"""
json---{“key”}
"""


"""
拓展：接口自动化时，字典与json格式字符串的转换
"""
import json
dictT = {'name':'tom','age':18}
print(dictT)
print(type(dictT))
print(json.dumps(dictT))


message ="""
{"name":"tom",
"age":18,
"height":176
}
"""
print(type(message))
print(json.loads(message))
res = json.loads(message)
res["name"]='hello'
print(type(json.loads(message)))
print(json.dumps(res))
