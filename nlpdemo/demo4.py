# -*- coding: gbk -*-
# @File  :
# @Date  : 2018/4/22
# @Software: PyCharm

import jieba
import os
import pickle  # �־û�
from numpy import *
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer  # TF-IDF����ת����
from sklearn.feature_extraction.text import TfidfVectorizer  # TF_IDF����������
from sklearn.datasets.base import Bunch
from sklearn.naive_bayes import MultinomialNB  # ����ʽ��Ҷ˹�㷨

#��ȡ�ı���Ϣ
def readFile(path):
    with open(path, 'r', errors='ignore') as file:  # �ĵ��б�����Щ���⣬������errors���˴���
        content = file.read()
        return content

#д���ı���Ϣ
def saveFile(path, result):
    with open(path, 'w', errors='ignore') as file:
        file.write(result)

#���ý�ͷִʽ����ı��ִ�
def segText(inputPath, resultPath):
    fatherLists = os.listdir(inputPath)  # ��Ŀ¼
    for eachDir in fatherLists:  # ������Ŀ¼�и����ļ���
        eachPath = inputPath + eachDir + "/"  # ������Ŀ¼��ÿ���ļ���Ŀ¼�����ڱ��������ļ�
        each_resultPath = resultPath + eachDir + "/"  # �ִʽ���ļ������Ŀ¼
        if not os.path.exists(each_resultPath):
            os.makedirs(each_resultPath)
        childLists = os.listdir(eachPath)  # ��ȡÿ���ļ����еĸ����ļ�
        for eachFile in childLists:  # ����ÿ���ļ����е����ļ�
            eachPathFile = eachPath + eachFile  # ���ÿ���ļ�·��
            #  print(eachFile)
            content = readFile(eachPathFile)  # �������溯����ȡ����
            # content = str(content)
            result = (str(content)).replace("\r\n", "").strip()  # ɾ�����������ո�
            # result = content.replace("\r\n","").strip()

            cutResult = jieba.cut(result)  # Ĭ�Ϸ�ʽ�ִʣ��ִʽ���ÿո����
            saveFile(each_resultPath + eachFile, " ".join(cutResult))  # �������溯�������ļ�

#���ý�ͷִʽ����ı��ִʣ������дʺ��list
def seg_doc(str_doc):
    # 1��������ԭ�ı�
    sent_list =str_doc.split(',')  # ���ݶ����з־���
    sent_list = map(textParse,sent_list)
    #2����ȡͣ�ô�
    stwlist = get_stop_words()
    #3���ִʲ�ȥ��ͣ�ô�
    word_2dlist = [rm_token(jieba.cut(part,cut_all=False),stwlist) for part in sent_list]
    #4���ϲ��б�
    word_list = sum(word_2dlist,[])
    return  word_list



#�ִ���������
def bunchSave(inputFile, outputFile):
    catelist = os.listdir(inputFile)
    bunch = Bunch(target_name=[], label=[], filenames=[], contents=[])
    bunch.target_name.extend(catelist)  # ����𱣴浽Bunch������
    for eachDir in catelist:
        eachPath = inputFile + eachDir + "/"
        fileList = os.listdir(eachPath)
        for eachFile in fileList:  # ����Ŀ¼�е�ÿ�����ļ�
            fullName = eachPath + eachFile  # ����Ŀ¼���ļ�ȫ·��
            bunch.label.append(eachDir)  # ��ǰ�����ǩ
            bunch.filenames.append(fullName)  # ���浱ǰ�ļ���·��
            bunch.contents.append(readFile(fullName).strip())  # �����ļ�������
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


def getStopWord(inputFile):
    stopWordList = readFile(inputFile).splitlines()
    return stopWordList


def getTFIDFMat(inputPath, stopWordList, outputPath):  # ���TF-IDF����
    bunch = readBunch(inputPath)
    tfidfspace = Bunch(target_name=bunch.target_name, label=bunch.label, filenames=bunch.filenames, tdm=[],
                       vocabulary={})
    # ��ʼ�������ռ�
    vectorizer = TfidfVectorizer(stop_words=stopWordList, sublinear_tf=True, max_df=0.5)
    transformer = TfidfTransformer()  # �����ͳ��ÿ�������TF-IDFȨֵ
    # �ı�ת��Ϊ��Ƶ���󣬵��������ֵ��ļ�
    tfidfspace.tdm = vectorizer.fit_transform(bunch.contents)
    tfidfspace.vocabulary = vectorizer.vocabulary_  # ��ȡ�ʻ�
    writeBunch(outputPath, tfidfspace)


def getTestSpace(testSetPath, trainSpacePath, stopWordList, testSpacePath):
    bunch = readBunch(testSetPath)
    # �������Լ�TF-IDF�����ռ�
    testSpace = Bunch(target_name=bunch.target_name, label=bunch.label, filenames=bunch.filenames, tdm=[],
                      vocabulary={})
    # ����ѵ�����Ĵʴ�
    trainbunch = readBunch(trainSpacePath)
    # ʹ��TfidfVectorizer��ʼ�������ռ�ģ��  ʹ��ѵ�����ʴ�����
    vectorizer = TfidfVectorizer(stop_words=stopWordList, sublinear_tf=True, max_df=0.5,
                                 vocabulary=trainbunch.vocabulary)
    transformer = TfidfTransformer()
    testSpace.tdm = vectorizer.fit_transform(bunch.contents)
    testSpace.vocabulary = trainbunch.vocabulary
    # �־û�
    writeBunch(testSpacePath, testSpace)


def bayesAlgorithm(trainPath, testPath):
    trainSet = readBunch(trainPath)
    testSet = readBunch(testPath)
    clf = MultinomialNB(alpha=0.001).fit(trainSet.tdm, trainSet.label)
    # alpha:0.001 alpha ԽС����������Խ�࣬����Խ��
    # print(shape(trainSet.tdm))  #������ʾ��������
    # print(shape(testSet.tdm))
    predicted = clf.predict(testSet.tdm)
    total = len(predicted)
    rate = 0
    for flabel, fileName, expct_cate in zip(testSet.label, testSet.filenames, predicted):
        if flabel != expct_cate:
            rate += 1
            print(fileName, ":ʵ�����", flabel, "-->Ԥ�����", expct_cate)
    print("erroe rate:", float(rate) * 100 / float(total), "%")


# �ִʣ���һ���Ƿִ����룬�ڶ��������ǽ�������·��
segText("C:/Users/wy/Desktop/data/", "C:/Users/wy/Desktop/segResult/")
bunchSave("C:/Users/wy/Desktop/segResult/", "C:/Users/wy/Desktop/train_set.dat")  # ����ִʣ�����ִ�����
stopWordList = getStopWord("C:/Users/wy/Desktop/stop/stopword.txt")  # ��ȡͣ�ô�
getTFIDFMat("C:/Users/wy/Desktop/train_set.dat", stopWordList, "C:/Users/wy/Desktop/tfidfspace.dat")  # �������������������ռ�

# ѵ����
segText("C:/Users/wy/Desktop/test1/", "C:/Users/wy/Desktop/test_segResult/")  # �ִ�
bunchSave("C:/Users/wy/Desktop/test_segResult/", "C:/Users/wy/Desktop/test_set.dat")
getTestSpace("C:/Users/wy/Desktop/test_set.dat", "C:/Users/wy/Desktop/tfidfspace.dat", stopWordList,
             "C:/Users/wy/Desktop/testspace.dat")
bayesAlgorithm("C:/Users/wy/Desktop/tfidfspace.dat", "C:/Users/wy/Desktop/testspace.dat")