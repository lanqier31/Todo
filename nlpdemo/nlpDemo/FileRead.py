# -*- coding: gbk -*-
# @File  :数据加载
# @Date  : 2020/4/27
# @Software: PyCharm
import os


def readFile(path):
    with open(path, 'r', errors='ignore') as file:  # 文档中编码有些问题，所有用errors过滤错误
        content = file.read()
    return content


# 写入文本信息
def saveFile(path, result):
    with open(path, 'w', errors='ignore') as file:
        file.write(result)
    file.close()



#遍历目录文件
def TraversalDir(rootDir):
    #返回指定目录包含的文件或文件夹的名字的列表
    for i,lists in enumerate(os.listdir(rootDir)):
        #待处理文件夹名字列表
        path = os.path.join(rootDir,lists)
        if os.path.isfile(path):
            yield path

        if os.path.isdir(path):
            TraversalDir(path)



#迭代器
class LoadFolders(object):
    def __init__(self,par_path):
        self.par_path = par_path

    def __iter__(self):
        for file in os.listdir(self.par_path):
            file_abspath = os.path.join(self.par_path,file)
            if os.path.isdir(file_abspath):
                yield file_abspath
            elif os.path.isfile(file_abspath):
                yield file


class LoadFiles(object):
    def __init__(self,par_path):
        self.par_path = par_path

    def __iter__(self):
        folders = LoadFolders(self.par_path)
        for folder in folders:
            if os.path.isdir(folder):
                 catg = folder.split(os.sep)[-1]
                 for file in os.listdir(folder):
                     # yield catg, file    #返回文件名
                     yield catg, os.path.join(folder, file),file  #返回文件路径 和文件名
            else:
                catg = folder.split('.')[0]
                yield catg,os.path.join(self.par_path, folder),folder


if __name__ == '__main__':
    path = r'../DataSet/cutText/'
    files = LoadFiles(path)
    for i,msg in enumerate(files):
        catg=msg[0]
        content = msg[1]
        content = readFile(content)
        print(content)







