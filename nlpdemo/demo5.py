# -*- coding: gbk -*-
# @File  :
# @Date  : 2018/4/22
# @Software: PyCharm

import jieba
import os
import pickle  # �־û�
from numpy import *
from nlpDemo.FileRead import LoadFolders,LoadFiles,TxtOperate
from nlpDemo.TextParse import textParse
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer  # TF-IDF����ת����
from sklearn.feature_extraction.text import TfidfVectorizer  # TF_IDF����������
from sklearn.datasets.base import Bunch
from sklearn.naive_bayes import MultinomialNB  # ����ʽ��Ҷ˹�㷨


if __name__ == '__main__':
    corpus_path = os.path.abspath(r'./DataSet/Syf/')
    segText_path = os.path.abspath(r'./DataSet/cutText/')
    files = LoadFiles(corpus_path)
    for i,msg in enumerate(files):
        catg = msg[0]
        content = msg[1]
        content = TxtOperate.readFile(content)
        content = textParse(content)   #������ϴ
        cutResult = jieba.cut(content)  #��ͷִ�
        TxtOperate.saveFile(segText_path+'/'+msg[2]," ".join(cutResult))  #�����д�







