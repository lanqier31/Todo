#coding:gbk
"""
Desc:�Զ�����ȡ�����ʣ�������������
"""
import jieba.posseg as  ps
from ProcessText.Stopword import *

def extract_feature(str_doc):
    feaWord = ""
    stop_words = get_stop_words()
    user_pos_list =['nr','ns','nt''nz']
    for word,pos in ps.cut(str_doc):
        if word not in stop_words and pos in user_pos_list:
            if word +' '+pos+'\n' not in feaWord:
                feaWord += word+' '+pos+'\n'
    print('����ʵ��ʶ��',feaWord)
    return feaWord



if __name__ == '__main__':
    path = r'../DataSet/Syf/BS/1.txt'
    str_doc = readFile(path)
    extract_feature(str_doc)
