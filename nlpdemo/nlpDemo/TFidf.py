# -*- coding: gbk -*-
# @File  :
# @Date  : 2018/4/22
# @Software: PyCharm

import jieba
import os
import pickle  # �־û�
from numpy import *
from nlpDemo.FileRead import LoadFolders,LoadFiles,readFile,saveFile
from nlpDemo.BunchSave import readBunch,writeBunch
from nlpDemo.TextParse import get_stop_words
from nlpDemo.TextParse import textParse
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer  # TF-IDF����ת����
from sklearn.feature_extraction.text import TfidfVectorizer  # TF_IDF����������
from sklearn.datasets.base import Bunch
from sklearn.naive_bayes import MultinomialNB  # ����ʽ��Ҷ˹�㷨


def getTFIDFMat(inputPath, stopWordList, outputPath,
                tftfidfspace_path,tfidfspace_arr_path,tfidfspace_vocabulary_path):  # ���TF-IDF����
    bunch = readBunch(inputPath)
    tfidfspace = Bunch(target_name=bunch.target_name, label=bunch.label, filenames=bunch.filenames, tdm=[],
                       vocabulary={})
    '''��ȡtfidfspace'''
    tfidfspace_out = str(tfidfspace)
    saveFile(tftfidfspace_path, tfidfspace_out)
    # ��ʼ�������ռ�
    vectorizer = TfidfVectorizer(stop_words=stopWordList, sublinear_tf=True, max_df=0.5)
    transformer = TfidfTransformer()  # �����ͳ��ÿ�������TF-IDFȨֵ
    # �ı�ת��Ϊ��Ƶ���󣬵��������ֵ��ļ�
    tfidfspace.tdm = vectorizer.fit_transform(bunch.contents)
    tfidfspace_arr = str(vectorizer.fit_transform(bunch.contents))
    saveFile(tfidfspace_arr_path, tfidfspace_arr)
    tfidfspace.vocabulary = vectorizer.vocabulary_  # ��ȡ�ʻ�
    tfidfspace_vocabulary = str(vectorizer.vocabulary_)
    saveFile(tfidfspace_vocabulary_path, tfidfspace_vocabulary)
    '''over'''
    writeBunch(outputPath, tfidfspace)


if __name__ == '__main__':
    train_dat_path = os.path.abspath(r'../DataSet/train_set.dat') #����ִʵĴ�����
    stopWordList = get_stop_words()
    tfidfspace_dat_path = os.path.abspath('../DataSet/tfidfspace.dat')  # tf-idf��Ƶ�ռ�������dat�ļ�
    tfidfspace_path = os.path.abspath(r'../DataSet/tfidfspace.txt') # �����Ƶ��Ϣtxt�ļ�
    tfidfspace_arr_path = os.path.abspath(r'../DataSet/tfidfspace_arr.txt')  # �����Ƶ����txt�ļ�
    tfidfspace_vocabulary_path = os.path.abspath(r'../DataSet/tfidfspace_vocabulary.txt')  # �������txt�ļ�

    getTFIDFMat(train_dat_path,  # ����ִʵĴ�����
                stopWordList,  # ��ȡͣ�ôʱ�
                tfidfspace_dat_path,  # tf-idf��Ƶ�ռ�������dat�ļ�
                tfidfspace_path,  # �����Ƶ��Ϣtxt�ļ�
                tfidfspace_arr_path,  # �����Ƶ����txt�ļ�
                tfidfspace_vocabulary_path)  # �������txt�ļ�




