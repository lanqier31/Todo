#coding:gbk
"""
Desc:����sklearn����tfidfֵ����
"""
from ProcessText.Stopword import *
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer

#����sklearn����tfidf������ȡ
def sklearn_tfidf_feature(corpus=None):
    vectorizer = CountVectorizer()  #�����ʻ��
    transformer = TfidfTransformer()  #ͳ��ÿ���ʵ�tfidf��Ȩֵ
    tfidf = transformer.fit_transform(vectorizer.fit_transform(corpus))
    print(tfidf)
    words = vectorizer.get_feature_names() #��ȡ�ʴ�ģ�������еĴ���
    print(words)
    #�������ȡ����
    # weight= tfidf.toarry()
    #
    # for i in range(len(weight)):
    #     print("------���������",i,"���ı��Ĵ�")
    #     for j in range(len(words)):
    #         print(words[j],weight[i][j])



if __name__ == '__main__':
    corpus=[]
    path1 = r'../DataSet/Syf/BS/1.txt'
    str_doc1 = readFile(path1)
    word_list1 =' '.join( seg_doc(str_doc1))

    path2 =r'../DataSet/Syf/BS/2.txt'
    str_doc2 = readFile(path2)
    word_list2 = ' '.join(seg_doc(str_doc2))
    corpus.append(word_list1)
    corpus.append(word_list2)

    # print(corpus)

    sklearn_tfidf_feature(corpus)
