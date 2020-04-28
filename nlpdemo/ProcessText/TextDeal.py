#coding:gbk
"""
Desc:文本数据处理实战
"""
from ProcessText.Stopword import *
from ClearText.EfficRead import *
import os,time



if __name__ == '__main__':
    startTime = time.time()

    filepath = os.path.abspath(r'../DataSet/Syf')
    files = loadFiles(filepath)
    for i,msg in enumerate(files):
        catg = msg[0]
        content = msg[1]
        content = readFile(content)
        print('{t}***{i} \t docs has been dealed'.format(i=i, t=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())),
              '\n', catg, ":\t", content[:20])

    endTime = time.time()
    print('totoal spend time: %.2f' %(endTime-startTime)+'s')