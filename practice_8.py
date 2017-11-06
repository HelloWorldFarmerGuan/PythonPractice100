#coding=utf-8
#输出 9*9 乘法口诀表。
for i in range(1,9):
    for j in range(1,9):
        print "%d*%d=%d" % (i, j, i * j),
        if i==j:
            print '\n'
            break;