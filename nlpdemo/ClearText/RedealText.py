#coding:gbk
"""
DESC: ������ϴ�ı�
prompt:coding in python3
"""
import re


#������ַ�������ϴ

def textParse(str_doc):
    #�������������ţ���㣬
    r1 = '[a-zA-Z0-9]'
    #ȥ���ո�
    r2='\s+'
    str_doc = re.sub(r2,str_doc)
    #ȥ�����з�
    str_doc = str_doc.replace('\n','')
    return str_doc



def readFile(path):
 str_doc = ""
 with open(path,'r') as f:
     str_doc = f.read()
 return str_doc

if __name__ == '__main__':
 path = r'../DataSet/Syf/BS/1.txt'

 str_doc = readFile(path)
 str_doc = textParse(str_doc)
 print(str_doc)
