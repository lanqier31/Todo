#coding:gbk
"""
Desc:自定义去停用词
"""
import re,sys
import jieba

#读取文本信息
def readFile(path):
    str_doc =""
    with open(path,'r') as f:
        str_doc=f.read()
    return str_doc

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



#利用结巴分词进行文本分词，返回切词后的list
def seg_doc(str_doc):
    # 1、正则处理原文本
    sent_list =str_doc.split(',')  # 根据逗号切分句子
    sent_list = map(textParse,sent_list)
    #2、获取停用词
    stwlist = get_stop_words()
    #3、分词并去除停用词
    word_2dlist = [rm_token(jieba.cut(part,cut_all=False),stwlist) for part in sent_list]
    #4、合并列表
    word_list = sum(word_2dlist,[])
    return  word_list


if __name__ == '__main__':

    path= r'../DataSet/Syf/BS/1.txt'
    str_doc = readFile(path)
    str_doc = textParse(str_doc)


    word_list = seg_doc(str_doc)

    print(word_list)