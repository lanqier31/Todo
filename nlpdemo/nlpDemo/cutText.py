# -*- coding: gbk -*-
# @File  :
# @Date  : 2018/4/22
# @Software: PyCharm

import jieba
import os
from numpy import *
from nlpDemo.FileRead import LoadFolders,LoadFiles,readFile, saveFile
from nlpDemo.TextParse import textParse




if __name__ == '__main__':
    corpus_path = os.path.abspath(r'./DataSet/Syf/')
    segText_path = os.path.abspath(r'./DataSet/cutText/')
    files = LoadFiles(corpus_path)
    for i,msg in enumerate(files):
        catg = msg[0]
        content = msg[1]
        content = readFile(content)
        content = textParse(content)   #数据清洗
        cutResult = jieba.cut(content)  #结巴分词
        saveFile(segText_path+'/'+msg[2]," ".join(cutResult))  #保存切词
