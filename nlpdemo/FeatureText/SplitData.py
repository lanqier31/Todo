#coding:gbk
"""
DESC: �з�����
prompt:coding in python3
"""

import os
from numpy import *

def file_matrix(filepath):
  file = open(filepath)
  arrayLines = file.readlines()
  print(arrayLines)

  returnMat = zeros((len(arrayLines),3))   #�������ݼ�
  # print(returnMat)
  classLabelMat =[]                        #��ǩ��
  index =0
  for line in arrayLines:       #���ж�ȡ��Ϣ
      listFromLine = line.strip().split('\t')  #��ʽ������ȥ���ո�ͨ��\t�ָ�
      returnMat[index,:] = listFromLine[0:3]      #��������ֻ��ȡǰ3��
      classLabelMat.append(int(listFromLine[-1]))
      index+=1
  return returnMat,classLabelMat






if __name__ == '__main__':

    filepath = os.path.abspath('../DataSet/dataset.txt')
    # file_matrix(filepath)
    returnMat, classMat = file_matrix(filepath)
    print(returnMat,classMat)












