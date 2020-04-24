#coding:gbk
"""
DESC:yield生成器案例
斐波那契数列：1,1,2,3,5,8,13,21...从数列的第三项开始，后面每一项是前面两项之和。
数学上的定义：F(0)=1,F(1)=1,...F(n)=F(n-1)+F(n-2)

"""
import time

#普通斐波那契数列数列实现
def fab(max):
    n,a,b = 0,0,1
    while n<max:
        # if n<20:
        #     print('->',b)
        a,b = b,a+b
        n= n+1

#生成器算法实现斐波那契数列  :效率快很多，几乎不花费时间
def fab2(max):
    n,a,b =0,0,1
    while n<max:
        yield b
        a,b =b,a+b
        n= n+1

def GenerateDemo():
    maxnum = 100000 #最大迭代数
    t1=time.time()
    fab2(maxnum)
    t2=time.time()
    print('Fab total time %.2f' % (1000*(t2-t1))+'ms')


if __name__ == '__main__':
    GenerateDemo()