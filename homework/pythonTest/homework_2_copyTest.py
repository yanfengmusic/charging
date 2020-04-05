#!/usr/bin/env python
# -*- coding: utf-8 -*-
import copy
__mtime__ = '2020-01-02'


"""
赋值
浅拷贝就是藕断丝连
深拷贝就是彻底离了

通常来讲不可变元素包含：
int,float,complex,long,str,unicode,tuple

浅拷贝：copy模块里面的copy方法实现
1、对象地址不变，还是原对象的地址
2、复制后，每个对象的元素的地址都是不变的，还是原对象的地址
3、如果在copy前对原对象中的值进行修改，如果原对象的值是可变的（比如数组），那么修改后，会影响copy后的值
4、如果在copy前对原对象中的值进行修改，如果原对象中的值是不可变的（比如字符串），那么修改后，则不会影响copy后的值
"""

#定义一个列表，其中第一个元素是可变类型。
# list1 = [[1,2],'fei',66]
#进行浅copy
# list2 = copy.copy(list1)
# print(list2)
# print(id(list1))
# print(id(list2))
#对象地址不同。2085203156424  2085203272328

#每一个元素地址是否相同。    结果：相同
# print(id(list1[0]))
# print(id(list2[0]))
# print(id(list1[1]))
# print(id(list2[1]))
# print(id(list1[2]))
# print(id(list2[2]))


# #改变第一个值,查看复制对象变化。
# list1[0][0] = 2
# print(list1)
# print(list2)
# 结果：复制对象发生变化
# [[2, 2], 'fei', 66]

# #改变第二个值,查看复制对象变化。
# list1[1] = 'ge'
# print(list2)
# #结果：复制对象没发生变化

"""
深拷贝：copy模块里面的deepcopy方法实现。
1、除了顶层拷贝，还对子元素也进行了拷贝。
2、经过深拷贝后，原始对象和拷贝对象所有的可变元素地址都没有相同的了。
3、说人话，就是深拷贝之后，生成了一个拥有新地址的新对象
4、copy后，改变原对象的值，不会影响新对象（因为新对象都是一个新地址了，所以改变不了）
"""

# #定义一个列表，其中第一个元素是可变类型。
list1 = [[1,2], 'fei', 66];
print(list1)
# #进行深copy
list2 = copy.deepcopy(list1)
#对象地址已经完全不同1527616249288  1527616365192
# print(id(list1))
# print(id(list2))
# print(list1)
# print(list2)

# 第一个元素地址是否相同？   不同
# print(id(list1[0]))
# print(id(list2[0]))

#第二个元素地址是否相同。   相同
# print(id(list1[1]));
# print(id(list2[1]));

# #改变第一个值,查看复制对象变化。  没有发生变化
# list1[0][0] = 2;
# print(list1)
# print(list2);

# #改变第二个值,查看复制对象变化。   没发生变化
list1[1] = 'ge'
print(list1)
print(list2)

