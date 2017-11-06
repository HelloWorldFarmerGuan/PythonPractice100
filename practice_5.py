#coding=utf-8
#输入三个整数x,y,z，请把这三个数由小到大输出。
a=int(raw_input('a:\n'))
b=int(raw_input('b:\n'))
c=int(raw_input('c:\n'))
l=[a,b,c]
flag=False
for i in range(len(l)):
    flag=False
    for j in range(len(l)-1):
        if l[j]>l[j+1]:
            temp=l[j]
            l[j]=l[j+1]
            l[j+1]=temp
            flag=True
    if flag==False:
        break;
print l