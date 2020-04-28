#coding:gbk
"""
Desc:nltk��Ƶѧϰ
"""
from nltk import *
from ProcessText.Stopword import readFile, seg_doc
import matplotlib
#���������ʾ,֮ǰĬ�ϵ����岻֧������
#1���鿴��ǰʹ�õ�����
#2����c/windows/fonts�µ��������帴�Ƶ�matplotlit/mpl-data/font/ttf �ļ�����
#3������ʹ������
matplotlib.rcParams['font.sans-serif'] = 'simhei'




#����nltk���д�Ƶ����ͳ��
def nltk_wf_feature(word_list=None):
    #��Ƶͳ�Ʒ���1
    fdlit = FreqDist(word_list)
    # print(fdlit.keys(),'\n',fdlit.values())  #keys:�ؼ��ʣ�values���ؼ��ʳ��ֵĴ���
    #
    # word = '��״��'
    # print(word,'����Ƶ�ʣ�',fdlit.freq(word))  #����������Ƶ��
    # print(word,'���ִ�����',fdlit[word])     #���������Ĵ���
    # print('***','Ƶ�ʷֲ���','***')
    # fdlit.tabulate(10)  # ��ȡ��������ǰ10���ʵ�Ƶ�ʷֲ���
    # print('***', 'Ƶ�ʷֲ�ͼ', '***')
    # fdlit.plot(30)
    return fdlit


if __name__ == '__main__':
    path = r'../DataSet/Syf/BS/1.txt'
    str_doc = readFile(path)
    print(str_doc)

    #2����Ƶ����ͳ��
    word_list = seg_doc(str_doc)
    nltk_wf_feature(word_list)

