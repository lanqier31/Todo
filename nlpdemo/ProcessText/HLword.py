#coding:gbk
"""
Desc:自定义高低词频
"""

from ProcessText.FreqWord import *
from ProcessText.Stopword import *

#选择高低词
def hl_freqword(fdist):
    wordlist=[]
    print('====')
    for key in fdist.keys():
        if fdist.get(key)>3 and fdist.get(key)<15:  #获取出现2次以上15次以下的关键词
            wordlist.append(key+":"+str(fdist.get(key)))
    return wordlist


if __name__ == '__main__':
    path = r'../DataSet/Syf/BS/1.txt'
    str_doc = readFile(path)
    word_list = seg_doc(str_doc)

    fdist = nltk_wf_feature(word_list)
    print(hl_freqword(fdist))







































