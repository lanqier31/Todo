#coding:gbk
"""
Desc:�Զ���ȥͣ�ô�
"""
import re,sys
import jieba

#��ȡ�ı���Ϣ

def readFile(path):
    str_doc =""
    with open(path,'r') as f:
        str_doc=f.read()
    return str_doc

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
        if words_list[i] in stop_words:
            words_list.pop(i)
        elif words_list[i].isdigit():
            words_list.pop(i)


#���ý�ͷִʽ����ı��ִʣ�
def seg_doc(str_doc):
    sent_list =str_doc.split(',')
    sent_list = map(textParse,sent_list)
    #��ȡͣ�ô�
    stwlist = get_stop_words()
    #�ִʲ�ȥ��ͣ�ô�
    word_2dlist = [rm_tokens(jieba.cut(part,cut_all=False)]



if __name__ == '__main__':

    path= r'../DataSet/Syf/BS/1.txt'
    str_doc = readFile(path)
    str_doc = textParse(str_doc)
    print(str_doc)