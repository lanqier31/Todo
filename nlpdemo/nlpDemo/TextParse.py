# -*- coding: gbk -*-
# @File  : ������ϴ
# @Date  : 2020/4/27
# @Software: PyCharm
import re

#�ı���ϴ
def textParse(str_doc):
    #ȥ���ַ�
    str_doc = re.sub('\u3000','',str_doc)
    str_doc = re.sub('\s+','',str_doc)  #ȥ���ո�
    str_doc = str_doc.replace('\n','')  #ȥ������

    return str_doc


#����ͣ�ô��б��
def get_stop_words(path=r'../DataSet/StopWord/nlp_stopwords.txt'):
    file = open(path,'r').read().split('\n')
    return set(file)  #ȥ��

#ȥ��ͣ�ôʺ�����
def rm_token(words,stwlist):
    """

    :param words: ��ͷִʷֺõĴ�
    :param stwlist: ͣ�ô��б�
    :return:
    """
    words_list = list(words)
    stop_words = stwlist
    for i in range(words_list.__len__())[::-1]:
        if words_list[i] in stop_words:      #ȥ��ͣ�ô�
            words_list.pop(i)
        elif words_list[i].isdigit():     #�ж��Ƿ�Ϊ����,������ȥ��
            words_list.pop(i)
        elif len(words_list[i])==1:     #ȥ�������ַ�
            words_list.pop(i)
        elif words_list[i] ==" ":   #ȥ���ո�
            words_list.pop(i)
    return words_list