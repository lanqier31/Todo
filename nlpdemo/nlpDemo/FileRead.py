# -*- coding: gbk -*-
# @File  :���ݼ���
# @Date  : 2020/4/27
# @Software: PyCharm
import os


def readFile(path):
    with open(path, 'r', errors='ignore') as file:  # �ĵ��б�����Щ���⣬������errors���˴���
        content = file.read()
    return content


# д���ı���Ϣ
def saveFile(path, result):
    with open(path, 'w', errors='ignore') as file:
        file.write(result)
    file.close()



#����Ŀ¼�ļ�
def TraversalDir(rootDir):
    #����ָ��Ŀ¼�������ļ����ļ��е����ֵ��б�
    for i,lists in enumerate(os.listdir(rootDir)):
        #�������ļ��������б�
        path = os.path.join(rootDir,lists)
        if os.path.isfile(path):
            yield path

        if os.path.isdir(path):
            TraversalDir(path)



#������
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
                     # yield catg, file    #�����ļ���
                     yield catg, os.path.join(folder, file),file  #�����ļ�·�� ���ļ���
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







