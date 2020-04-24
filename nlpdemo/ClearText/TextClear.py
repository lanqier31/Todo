#coding:gbk
"""
DESC: 文本数据的清洗
prompt:coding in python3
"""
import re,os,time
from RedealText import textParse


# 高效读取文件
#迭代器
class loadFolders(object):
    def __init__(self,par_path):
        self.par_path = par_path

    def __iter__(self):
        for file in os.listdir(self.par_path):
            file_abspath = os.path.join(self.par_path,file)
            if os.path.isdir(file_abspath):
                yield file_abspath


class loadFiles(object):
    def __init__(self,par_path):
        self.par_path = par_path

    def __iter__(self):
        folders = loadFolders(self.par_path)
        for folder in folders:
             catg = folder.split(os.sep)[-1]
             for file in os.listdir(folder):
                 file_path  = os.path.join(folder,file)
                 if os.path.isfile(file_path):
                     this_file = open(file_path,'rb')
                     content =this_file.read().decode('gbk')

                 yield catg, content
                 this_file.close()

if __name__ == '__main__':
    start = time.time()
    file_path =r'../DataSet/Syf/'
    files = loadFiles(file_path)
    n=3   #抽样
    for i,msg in enumerate(files):
        catg = msg[0]
        content = msg[1]
        # content = textParse(content)
        print('{t}***{i} \t docs has been dealed'.format(i=i,t=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())),'\n',catg,":\t",content[:20])

    end = time.time()
    print("total spend time: %.2f" %(end-start)+'s')



