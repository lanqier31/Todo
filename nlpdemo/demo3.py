#coding: gbk

from pyhanlp import *
"""hanlp 分词不好用，java与python 位数配置麻烦"""

sentence = "我爱自然语言处理技术！"
s_hanlp = HanLP.segment(sentence)
for term in s_hanlp:
    print(term.word, term.nature)
