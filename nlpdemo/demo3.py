#coding: gbk

from pyhanlp import *
"""hanlp �ִʲ����ã�java��python λ�������鷳"""

sentence = "�Ұ���Ȼ���Դ�������"
s_hanlp = HanLP.segment(sentence)
for term in s_hanlp:
    print(term.word, term.nature)
