#coding:gbk
"""
Desc:�Զ���ߵʹ�Ƶ
"""

from ProcessText.FreqWord import *
from ProcessText.Stopword import *

#ѡ��ߵʹ�
def hl_freqword(fdist):
    wordlist=[]
    print('====')
    for key in fdist.keys():
        if fdist.get(key)>3 and fdist.get(key)<15:  #��ȡ����2������15�����µĹؼ���
            wordlist.append(key+":"+str(fdist.get(key)))
    return wordlist


if __name__ == '__main__':
    path = r'../DataSet/Syf/BS/1.txt'
    str_doc = readFile(path)
    word_list = seg_doc(str_doc)

    fdist = nltk_wf_feature(word_list)
    print(hl_freqword(fdist))







































