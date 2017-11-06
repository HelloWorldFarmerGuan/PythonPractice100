#coding=utf-8
#古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？
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