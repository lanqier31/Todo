# -*- coding: gbk -*-
# @File  :
# @Date  : 2018/4/22
# @Software: PyCharm

import jieba
import os
import pickle  # 持久化
from numpy import *
from nlpDemo.FileRead import LoadFolders,LoadFiles,readFile,saveFile
from nlpDemo.BunchSave import readBunch,writeBunch
from nlpDemo.TextParse import get_stop_words
from nlpDemo.TextParse import textParse
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer  # TF-IDF向量转换类
from sklearn.feature_extraction.text import TfidfVectorizer  # TF_IDF向量生成类
from sklearn.datasets.base import Bunch
from sklearn.naive_bayes import MultinomialNB  # 多项式贝叶斯算法


def getTFIDFMat(inputPath, stopWordList, outputPath,
                tftfidfspace_path,tfidfspace_arr_path,tfidfspace_vocabulary_path):  # 求得TF-IDF向量
    bunch = readBunch(inputPath)
    tfidfspace = Bunch(target_name=bunch.target_name, label=bunch.label, filenames=bunch.filenames, tdm=[],
                       vocabulary={})
    '''读取tfidfspace'''
    tfidfspace_out = str(tfidfspace)
    saveFile(tftfidfspace_path, tfidfspace_out)
    # 初始化向量空间
    vectorizer = TfidfVectorizer(stop_words=stopWordList, sublinear_tf=True, max_df=0.5)
    transformer = TfidfTransformer()  # 该类会统计每个词语的TF-IDF权值
    # 文本转化为词频矩阵，单独保存字典文件
    tfidfspace.tdm = vectorizer.fit_transform(bunch.contents)
    tfidfspace_arr = str(vectorizer.fit_transform(bunch.contents))
    saveFile(tfidfspace_arr_path, tfidfspace_arr)
    tfidfspace.vocabulary = vectorizer.vocabulary_  # 获取词汇
    tfidfspace_vocabulary = str(vectorizer.vocabulary_)
    saveFile(tfidfspace_vocabulary_path, tfidfspace_vocabulary)
    '''over'''
    writeBunch(outputPath, tfidfspace)


if __name__ == '__main__':
    train_dat_path = os.path.abspath(r'../DataSet/train_set.dat') #读入分词的词向量
    stopWordList = get_stop_words()
    tfidfspace_dat_path = os.path.abspath('../DataSet/tfidfspace.dat')  # tf-idf词频空间向量的dat文件
    tfidfspace_path = os.path.abspath(r'../DataSet/tfidfspace.txt') # 输出词频信息txt文件
    tfidfspace_arr_path = os.path.abspath(r'../DataSet/tfidfspace_arr.txt')  # 输出词频矩阵txt文件
    tfidfspace_vocabulary_path = os.path.abspath(r'../DataSet/tfidfspace_vocabulary.txt')  # 输出单词txt文件

    getTFIDFMat(train_dat_path,  # 读入分词的词向量
                stopWordList,  # 获取停用词表
                tfidfspace_dat_path,  # tf-idf词频空间向量的dat文件
                tfidfspace_path,  # 输出词频信息txt文件
                tfidfspace_arr_path,  # 输出词频矩阵txt文件
                tfidfspace_vocabulary_path)  # 输出单词txt文件




