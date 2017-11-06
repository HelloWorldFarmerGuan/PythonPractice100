#coding=utf-8
#判断101-200之间有多少个素数，并输出所有素数。
from math import sqrt

nums=[]
flag=True;
for i in range(101,200):
    for j in range(2,int(sqrt(i)+1)):
        if i%j==0:
            flag=False
            break;
    if flag==True:
        nums.append(i)
    flag=True

print nums,'total:',len(nums)