#coding=utf-8
#将一个列表的数据复制到另一个列表中。
import copy

a=[1,2,3,4,5]
b1=a
b2=a[:]
b3=copy.copy(a);
a.append(6)
print (b1, b2,b3)