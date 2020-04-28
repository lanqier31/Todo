# -*- coding: gbk -*-
# @File  :
# @Date  : 2018/4/22
# @Software: PyCharm

import jieba
import os
import pickle  # 持久化
from numpy import *
from nlpDemo.FileRead import LoadFolders,LoadFiles,TxtOperate
from nlpDemo.TextParse import textParse
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer  # TF-IDF向量转换类
from sklearn.feature_extraction.text import TfidfVectorizer  # TF_IDF向量生成类
from sklearn.datasets.base import Bunch
from sklearn.naive_bayes import MultinomialNB  # 多项式贝叶斯算法


if __name__ == '__main__':
    corpus_path = os.path.abspath(r'./DataSet/Syf/')
    segText_path = os.path.abspath(r'./DataSet/cutText/')
    files = LoadFiles(corpus_path)
    for i,msg in enumerate(files):
        catg = msg[0]
        content = msg[1]
        content = TxtOperate.readFile(content)
        content = textParse(content)   #数据清洗
        cutResult = jieba.cut(content)  #结巴分词
        TxtOperate.saveFile(segText_path+'/'+msg[2]," ".join(cutResult))  #保存切词







