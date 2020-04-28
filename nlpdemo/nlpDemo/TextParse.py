# -*- coding: gbk -*-
# @File  : 数据清洗
# @Date  : 2020/4/27
# @Software: PyCharm
import re

#文本清洗
def textParse(str_doc):
    #去除字符
    str_doc = re.sub('\u3000','',str_doc)
    str_doc = re.sub('\s+','',str_doc)  #去除空格
    str_doc = str_doc.replace('\n','')  #去除换行

    return str_doc


#创建停用词列表表
def get_stop_words(path=r'../DataSet/StopWord/nlp_stopwords.txt'):
    file = open(path,'r').read().split('\n')
    return set(file)  #去重

#去除停用词和数字
def rm_token(words,stwlist):
    """

    :param words: 结巴分词分好的词
    :param stwlist: 停用词列表
    :return:
    """
    words_list = list(words)
    stop_words = stwlist
    for i in range(words_list.__len__())[::-1]:
        if words_list[i] in stop_words:      #去除停用词
            words_list.pop(i)
        elif words_list[i].isdigit():     #判断是否为数字,若是则去除
            words_list.pop(i)
        elif len(words_list[i])==1:     #去除单个字符
            words_list.pop(i)
        elif words_list[i] ==" ":   #去除空格
            words_list.pop(i)
    return words_list