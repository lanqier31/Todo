# -*- coding: gbk -*-
# @File  :
# @Date  : 2018/4/22
# @Software: PyCharm

import jieba
import os
import pickle  # �־û�
from numpy import *
from nlpDemo.FileRead import LoadFolders,LoadFiles,readFile,saveFile
from nlpDemo.TextParse import textParse
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer  # TF-IDF����ת����
from sklearn.feature_extraction.text import TfidfVectorizer  # TF_IDF����������
from sklearn.datasets.base import Bunch
from sklearn.naive_bayes import MultinomialNB  # ����ʽ��Ҷ˹�㷨



#�ִ���������
def bunchSave(inputFile, outputFile):
    catelist = os.listdir(inputFile)
    bunch = Bunch(target_name=[], label=[], filenames=[], contents=[])
    bunch.target_name.extend(catelist)  # ����𱣴浽Bunch������
    files = LoadFiles(inputFile)
    for i,msg in enumerate(files):
        bunch.label.append(msg[0]) # ��ǰ�����ǩ
        bunch.filenames.append(msg[1])  # ���浱ǰ�ļ���·��
        bunch.contents.append(readFile(msg[1]).strip())  # �����ļ�������

    with open(outputFile, 'wb') as file_obj:  # �־û������ö����Ʒ���ģʽ��
        pickle.dump(bunch, file_obj)
        # pickle.dump(obj, file, [,protocol])�����Ĺ��ܣ���obj�������л������Ѿ��򿪵�file�С�
        # obj����Ҫ���л���obj����
        # file:�ļ����ơ�
        # protocol�����л�ʹ�õ�Э�顣�������ʡ�ԣ���Ĭ��Ϊ0�����Ϊ��ֵ��HIGHEST_PROTOCOL����ʹ����ߵ�Э��汾


def readBunch(path):
    with open(path, 'rb') as file:
        bunch = pickle.load(file)
        # pickle.load(file)
        # �����Ĺ��ܣ���file�еĶ������л�������
    return bunch


def writeBunch(path, bunchFile):
    with open(path, 'wb') as file:
        pickle.dump(bunchFile, file)


if __name__ == '__main__':
    split_datapath = os.path.abspath(r'../DataSet/cutText/')
    train_dat_path = os.path.abspath(r'../DataSet/train_set.dat')
    bunchSave(split_datapath,train_dat_path)

