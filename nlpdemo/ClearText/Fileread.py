#coding:gbk
"""
DESC: �ݹ�������ȡ�ı���Ϣ
prompt:coding in python3
"""
import os,time


#����Ŀ¼�ļ�
def TraversalDir(rootDir):
    #����ָ��Ŀ¼�������ļ����ļ��е����ֵ��б�
    for i,lists in enumerate(os.listdir(rootDir)):
        #�������ļ��������б�
        path = os.path.join(rootDir,lists)
        if os.path.isfile(path):
            print('{t}***{i} \t docs has been read'.format(i=i,t= time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())))

        if os.path.isdir(path):
            TraversalDir(path)


if __name__ == '__main__':
    rootDir = r'../Dataset/Syf/'
    t1=time.time()
    TraversalDir(rootDir)
    t2=time.time()
    print('Total cost time %.2f'%(t2-t1)+'s')





