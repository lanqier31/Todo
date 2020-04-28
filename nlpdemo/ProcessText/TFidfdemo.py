#coding:gbk
"""
Desc:利用sklearn计算tfidf值特征
"""
from ProcessText.Stopword import *
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer

#利用sklearn计算tfidf特征提取
def sklearn_tfidf_feature(corpus=None):
    vectorizer = CountVectorizer()  #构建词汇表
    transformer = TfidfTransformer()  #统计每个词的tfidf的权值
    tfidf = transformer.fit_transform(vectorizer.fit_transform(corpus))
    print(tfidf)
    words = vectorizer.get_feature_names() #获取词袋模型中所有的词语
    print(words)
    #将矩阵抽取出来
    # weight= tfidf.toarry()
    #
    # for i in range(len(weight)):
    #     print("------这里输出第",i,"类文本的词")
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
