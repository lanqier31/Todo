#coding: gbk
import  jieba
import jieba.analyse

jieba.load_userdict('./Database/Sample/dict.txt')

text = u'''
��IIa-III���ɼ�2ö�ͻ�����ڣ���һλ�ھ��ܶ����ֲ洦ǰ��࣬��СԼ1.47*0.44cm�����壬��̬����Ƥ���ʽṹ�塣 
��III-IV���ɼ�2ö�ͻ�����ڣ���һλ�ھ��ھ�����࣬��СԼ0.96*0.24cm�����壬��̬����Ƥ���ʽṹ�塣 
��IV���ɼ��෢�ͻ�����ڣ���һλ�ھ��ھ����󷽣���СԼ0.49*0.19cm�����壬��̬����Ƥ���ʽṹ�塣
��������������Ͽɼ�һ�ͻ�����ڣ���СԼ0.53*0.38cm�����壬��̬����������Բ�Σ�Ƥ���ʽṹ��Լ�ɼ����ɼ�Ѫ���źš� 
��VI����״����Ҷ�·��ɼ�һ�ͻ�����ڣ���СԼ0.54*0.41cm�������壬����Բ�Σ�Ƥ���ʽṹ���壬�ڿɼ��෢��״ǿ������Ѫ���ḻ����
'''

# seg_list = jieba.cut(text,cut_all=False) # cut_all�Ĳ�����TrueΪȫģʽ  :�з�̫ϸ��False Ϊ��ȷģʽ��Ĭ��Ϊ��ȷģʽ
# print("Full Mode: " + "/ ".join(seg_list))

keywords = jieba.analyse.extract_tags(text)
print("/".join(keywords))

keywords2 = jieba.analyse.TFIDF(idf_path=None)
print(keywords2)

# seg_list2 = jieba.cut_for_search(text) #��������ģʽ
# for s in seg_list2:
#     print(s)