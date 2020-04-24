import os,time
from datetime import datetime
from openpyxl import load_workbook
import pandas as pd
from aip import AipOcr

""" 你的 APPID AK SK """
APP_ID = '11530950'
API_KEY = 'AHZIWWZhG71ic0ZDUfyXDidw'
SECRET_KEY = 'SP8aYSaNBc55yF3YkR4sGahMlGpq8NQf'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

file_dir=r'imgs/'
"""从目录中获取图片"""
def file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        # print(root) #当前目录路径
        # return dirs #当前路径下所有子目录
        return files #当前路径下所有非目录子文件

""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

"""记录request_id"""
def log_txt(data):
    with open("data.txt","a+") as f:
        f.writelines(data+'\n')

"""读取txt"""
def readtxt(filepath):
    with open(filepath, 'r') as f:
        res = []
        while True:
            lines = f.readline()  # 整行读取数据
            if not lines:
                break
            p_tmp = [i.replace(u'\n', '') for i in lines.split(":")]  # 将整行数据分割处理，如果分割符是空格，括号里就不用传入参数，如果是逗号， 则传入‘，'字符。
            res.append(p_tmp)
        return dict(res)

now = datetime.now().strftime("%Y%m%d%H%M%S")
excelPath = r'gene'+now+'.xlsx'
excelWriter = pd.ExcelWriter(excelPath, engine='openpyxl')
imgs = file_name(file_dir)
if len(imgs)==0:
    print('not exist images')
else:
    for img in imgs:
        img_path=file_dir+img
        image = get_file_content(img_path)
        img = img.replace('.png', '').replace('.jpg', '')
        total={}
        t1,t2,t3,t4,t5,t6,t7,key=[],[],[],[],[],[],[],[]

        """ 调用自定义模板文字识别 """
        client.custom(image);

        """ 如果有可选参数 """
        options = {}
        options["templateSign"] = "3f8c7bd213fbe2e82d4f3881f450fdb1"  #3突变模板
        # options["classifierId"] = 31232   指定分类器

        """ 带参数调用自定义模板文字识别 """
        result = client.custom(image, options)['data']['ret']
        for r in result:
            word_name = r['word_name'].split("#")[-1]
            word=r['word']
            if word_name not in key:
                key.append(word_name)
            if word_name=='基因':
                t1.append(r['word'] if len(r['word'])> 0 else u'/')
            if word_name=='转录本编号':
                t2.append(r['word']if len(r['word'])> 0 else u'/')
            if word_name=='外显子位置':
                t3.append(r['word']if len(r['word'])> 0 else u'/')
            if word_name=='核苷酸变化':
                t4.append(r['word']if len(r['word'])> 0 else u'/')
            if word_name=='氨基酸变化':
                t5.append(r['word']if len(r['word'])> 0 else u'/')
            if word_name=='dbSNP':
                t6.append(r['word']if len(r['word'])> 0 else u'/')
            if word_name == '突变比例':
                t7.append(r['word']if len(r['word'])> 0 else u'/')
        total=dict(zip(key,[t1,t2,t3,t4,t5,t6,t7]))
        df = pd.DataFrame(total)
        df.to_excel(excelWriter, sheet_name=img)
        excelWriter.save()