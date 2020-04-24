#coding:gbk
"""
DESC:yield����������
쳲��������У�1,1,2,3,5,8,13,21...�����еĵ����ʼ������ÿһ����ǰ������֮�͡�
��ѧ�ϵĶ��壺F(0)=1,F(1)=1,...F(n)=F(n-1)+F(n-2)

"""
import time

#��ͨ쳲�������������ʵ��
def fab(max):
    n,a,b = 0,0,1
    while n<max:
        # if n<20:
        #     print('->',b)
        a,b = b,a+b
        n= n+1

#�������㷨ʵ��쳲���������  :Ч�ʿ�ܶ࣬����������ʱ��
def fab2(max):
    n,a,b =0,0,1
    while n<max:
        yield b
        a,b =b,a+b
        n= n+1

def GenerateDemo():
    maxnum = 100000 #��������
    t1=time.time()
    fab2(maxnum)
    t2=time.time()
    print('Fab total time %.2f' % (1000*(t2-t1))+'ms')


if __name__ == '__main__':
    GenerateDemo()