#coding:gbk
"""
DESC: 递归批量读取文本信息
prompt:coding in python3
"""
import os,time


#遍历目录文件
def TraversalDir(rootDir):
    #返回指定目录包含的文件或文件夹的名字的列表
    for i,lists in enumerate(os.listdir(rootDir)):
        #待处理文件夹名字列表
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





