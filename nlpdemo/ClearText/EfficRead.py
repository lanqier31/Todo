#coding:gbk
"""
DESC: 高效读取文本信息
prompt:coding in python3
"""
import os,time


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
                 yield catg, file


if __name__ == '__main__':
    start = time.time()
    filepath = os.path.abspath(r'../DataSet/Syf/')
    files = loadFiles(filepath)
    for i,msg in enumerate(files):
        print('{t}***{i}\t docs has been read'.format(i=i,t= time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())))
    end = time.time()
    print('Total cost time:%.2f' %(end-start)+'s')


