#coding=utf-8
#将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。
import prime as prime

nums=[]
int_num=int(raw_input('Integer:\n'))

def reduceNum(num):
    falg = False
    for i in range(2,num):
        if num%i==0:
            nums.append(i)
            reduceNum(num/i)
            falg=True
            break;
    if  falg==False:
        nums.append(num)

def formatNum(nums):
    formatN=str(int_num)+"="
    for i in range(0,len(nums)):
        if i!=len(nums)-1:
            formatN=formatN+str(nums[i])+"*"
        else:
            formatN=formatN+str(nums[i])
    return formatN
reduceNum(int_num)
print formatNum(nums)


