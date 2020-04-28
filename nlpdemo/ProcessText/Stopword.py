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

#�ı���ϴ
def textParse(str_doc):
    #ȥ���ַ�
    str_doc = re.sub('\u3000','',str_doc)
    str_doc = re.sub('\s+','',str_doc)  #ȥ���ո�
    str_doc = str_doc.replace('\n','')  #ȥ������

    return str_doc

#����ͣ�ô��б���
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


if __name__ == '__main__':

    path= r'../DataSet/Syf/BS/1.txt'
    str_doc = readFile(path)
    str_doc = textParse(str_doc)


    word_list = seg_doc(str_doc)

    print(word_list)