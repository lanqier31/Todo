#coding:gbk
"""
DESC: 正则清洗文本
prompt:coding in python3
"""
import re


#正则对字符串的清洗

def textParse(str_doc):
    #正则过滤特殊符号，标点，
    r1 = '[a-zA-Z0-9]'
    #去除空格
    r2='\s+'
    str_doc = re.sub(r2,str_doc)
    #去除换行符
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
