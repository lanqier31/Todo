#coding:gbk
"""
Desc:nltk词频学习
"""
from nltk import *
from ProcessText.Stopword import readFile, seg_doc
import matplotlib
#解决中文显示,之前默认的字体不支持中文
#1、查看当前使用的字体
#2、将c/windows/fonts下的中文字体复制到matplotlit/mpl-data/font/ttf 文件夹下
#3、设置使用字体
matplotlib.rcParams['font.sans-serif'] = 'simhei'




#利用nltk进行词频特征统计
def nltk_wf_feature(word_list=None):
    #词频统计方法1
    fdlit = FreqDist(word_list)
    # print(fdlit.keys(),'\n',fdlit.values())  #keys:关键词；values：关键词出现的次数
    #
    # word = '甲状腺'
    # print(word,'出现频率：',fdlit.freq(word))  #给定样本的频率
    # print(word,'出现次数：',fdlit[word])     #给定样本的次数
    # print('***','频率分布表','***')
    # fdlit.tabulate(10)  # 读取出现最多的前10个词的频率分布表
    # print('***', '频率分布图', '***')
    # fdlit.plot(30)
    return fdlit


if __name__ == '__main__':
    path = r'../DataSet/Syf/BS/1.txt'
    str_doc = readFile(path)
    print(str_doc)

    #2、词频特征统计
    word_list = seg_doc(str_doc)
    nltk_wf_feature(word_list)

