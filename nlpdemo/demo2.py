#coding: gbk
import os
import time
import random
import jieba
import nltk
import sklearn
from sklearn.naive_bayes import MultinomialNB
import numpy as np
# import pylab as pl
# import matplotlib.pyplot as plt
#�ֱ��Ĵ�ȥ��
def make_word_set(words_file):
    words_set = set()
    with open(words_file, 'r',encoding='gbk') as fp:
        for line in fp.readlines():
            word = line.strip()  #word = line.strip().decode("utf-8")
            if len(word)>0 and word not in words_set: # ȥ��
                words_set.add(word)
    return words_set


# �ı�����Ҳ�����������ɹ���
def text_processing(folder_path, test_size=0.2):
    folder_list = os.listdir(folder_path)
    data_list = []
    class_list = []

    # �����ļ���
    for folder in folder_list:
        new_folder_path = os.path.join(folder_path, folder)
        files = os.listdir(new_folder_path)
        # ��ȡ�ļ�
        j = 1
        for file in files:
            if j > 100:  # ���ڴ汬����ֻȡ100�������ļ�
                break
            with open(os.path.join(new_folder_path, file), 'r', encoding='gbk') as fp:
                raw = fp.read()
            ## jieba���ķִ�
            #jieba.enable_parallel(4)  # �������зִ�ģʽ������Ϊ���н���������֧��windows
            word_cut = jieba.cut(raw, cut_all=False)  # ��ȷģʽ
            word_list = list(word_cut)  # genertorת��Ϊlist��ÿ����unicode��ʽ
            #jieba.disable_parallel()  # �رղ��зִ�ģʽ

            data_list.append(word_list)  # ѵ����list
            class_list.append(folder.encode('gbk'))  # ��� class_list.append(folder.decode('utf-8'))
            j += 1

    ## ����ѵ�����Ͳ��Լ�
    data_class_list = list(zip(data_list, class_list)) #data_class_list = zip(data_list, class_list)
    random.shuffle(data_class_list)
    index = int(len(data_class_list) * test_size) + 1
    train_list = data_class_list[index:]
    test_list = data_class_list[:index]
    train_data_list, train_class_list = zip(*train_list)
    test_data_list, test_class_list = zip(*test_list)

    # ͳ�ƴ�Ƶ����all_words_dict
    all_words_dict = {}
    for word_list in train_data_list:
        for word in word_list:
            if all_words_dict.get(word)!=None:  #if all_words_dict.has_key(word):
                all_words_dict[word] += 1
            else:
                all_words_dict[word] = 1

    # ��Ƶ���н�������
    all_words_tuple_list = sorted(all_words_dict.items(), key=lambda f: f[1], reverse=True)  # �ڽ�����sorted������Ϊlist
    all_words_list = list(list(zip(*all_words_tuple_list))[0]) #all_words_list = list(zip(*all_words_tuple_list)[0])

    return all_words_list, train_data_list, test_data_list, train_class_list, test_class_list


def words_dict(all_words_list, deleteN, stopwords_set=set()):
    # ѡȡ������
    feature_words = []
    n = 1
    for t in range(deleteN, len(all_words_list), 1):
        if n > 1000:  # feature_words��ά��1000
            break

        if not all_words_list[t].isdigit() and all_words_list[t] not in stopwords_set and 1 < len(
                all_words_list[t]) < 5:
            feature_words.append(all_words_list[t])
            n += 1
    return feature_words

# �ı�����
def text_features(train_data_list, test_data_list, feature_words, flag='nltk'):
    def text_features(text, feature_words):
        text_words = set(text)
        ## -----------------------------------------------------------------------------------
        if flag == 'nltk':
            ## nltk���� dict
            features = {word:1 if word in text_words else 0 for word in feature_words}
        elif flag == 'sklearn':
            ## sklearn���� list
            features = [1 if word in text_words else 0 for word in feature_words]
        else:
            features = []
        ## -----------------------------------------------------------------------------------
        return features
    train_feature_list = [text_features(text, feature_words) for text in train_data_list]
    test_feature_list = [text_features(text, feature_words) for text in test_data_list]
    return train_feature_list, test_feature_list

# ���࣬ͬʱ���׼ȷ�ʵ�
def text_classifier(train_feature_list, test_feature_list, train_class_list, test_class_list, flag='nltk'):
    ## -----------------------------------------------------------------------------------
    if flag == 'nltk':
        ## ʹ��nltk������
        train_flist = zip(train_feature_list, train_class_list)
        test_flist = zip(test_feature_list, test_class_list)
        classifier = nltk.classify.NaiveBayesClassifier.train(train_flist)
        test_accuracy = nltk.classify.accuracy(classifier, test_flist)
    elif flag == 'sklearn':
        ## sklearn������
        classifier = MultinomialNB().fit(train_feature_list, train_class_list)
        test_accuracy = classifier.score(test_feature_list, test_class_list)
    else:
        test_accuracy = []
    return test_accuracy


print("start")

## �ı�Ԥ����
folder_path = r'Database/Sample'
all_words_list, train_data_list, test_data_list, train_class_list, test_class_list = text_processing(folder_path, test_size=0.2)

# ����stopwords_set
stopwords_file = 'stopwords_cn.txt'
stopwords_set = make_word_set(stopwords_file)

## �ı�������ȡ�ͷ���
# flag = 'nltk'
flag = 'sklearn'
deleteNs = range(0, 1000, 20)
test_accuracy_list = []
for deleteN in deleteNs:
    # feature_words = words_dict(all_words_list, deleteN)
    feature_words = words_dict(all_words_list, deleteN, stopwords_set)
    train_feature_list, test_feature_list = text_features(train_data_list, test_data_list, feature_words, flag)
    test_accuracy = text_classifier(train_feature_list, test_feature_list, train_class_list, test_class_list, flag)
    test_accuracy_list.append(test_accuracy)
print(test_accuracy_list)

# �������
#plt.figure()
# plt.plot(deleteNs, test_accuracy_list)
# # plt.title('Relationship of deleteNs and test_accuracy')
# # plt.xlabel('deleteNs')
# # plt.ylabel('test_accuracy')
# # #plt.show()
# # plt.savefig('result.png')

print("finished")
