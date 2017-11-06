#coding=utf-8
#斐波那契数列。斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。

def fun(n):
    a = 0
    b = 1
    if n==1:
        return a
    elif n==2:
        return b
    else:
        for i in range(n-2):
            temp=a
            a=b
            b=a+temp
        return b

print fun(10)