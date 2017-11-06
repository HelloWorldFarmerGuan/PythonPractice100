#coding=utf-8
#利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。
score=int(raw_input('分数:\n'))
if score>=90:
    print '等级:A'
elif score>=60 and score<90:
    print '等级:B'
elif score>=0 and score<60:
    print '等级:C'
else :
    print '请输入正确分数'