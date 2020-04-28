#coding:gbk
"""
DESC: 切分数据
prompt:coding in python3
"""

import os
from numpy import *

def file_matrix(filepath):
  file = open(filepath)
  arrayLines = file.readlines()
  print(arrayLines)

  returnMat = zeros((len(arrayLines),3))   #特征数据集
  # print(returnMat)
  classLabelMat =[]                        #标签集
  index =0
  for line in arrayLines:       #朱行读取信息
      listFromLine = line.strip().split('\t')  #格式化处理：去掉空格，通过\t分割
      returnMat[index,:] = listFromLine[0:3]      #特征矩阵，只获取前3列
      classLabelMat.append(int(listFromLine[-1]))
      index+=1
  return returnMat,classLabelMat






if __name__ == '__main__':

    filepath = os.path.abspath('../DataSet/dataset.txt')
    # file_matrix(filepath)
    returnMat, classMat = file_matrix(filepath)
    print(returnMat,classMat)












