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
resId=[]
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
# if not os.path.exists(excelPath):
#     os.mkdir(excelPath)
excelWriter = pd.ExcelWriter(excelPath, engine='openpyxl')
imgs = file_name(file_dir)
if len(imgs)==0:
    print('not exist images')
else:
    for img in imgs:
        im = img.replace('.png', '').replace('.jpg', '')
        if im in readtxt(r'data.txt'):
            requestId =readtxt(r'data.txt')[im]
        else:
            img_path=file_dir+img
            image = get_file_content(img_path)
            """ 调用表格文字识别同步接口 """
            client.form(image);
            # try:
            requestId = client.tableRecognitionAsync(image)['result'][0]['request_id']
            resId.append(requestId)
            log_txt(img+':'+requestId)
        """ 调用表格识别结果 """
        options = {}
        options["result_type"] = "json"
        result = client.getTableRecognitionResult(requestId, options)
        while True:
            result = client.getTableRecognitionResult(requestId, options)
            if result.get('error_code'):
                print('Open api qps request limit reached')
                os.exit()  #终止程序
            elif result['result']['ret_msg']==u'进行中':
                time.sleep(3)
            else:
                break
        datas = eval(result['result']['result_data'])['forms'][0]['body']
        max_column = datas[-1]['column'][0]
        t = []
        temp = {}
        for i in range(1, max_column):
            for rect in datas:
                if rect['column'][0] == i:
                    t.append(rect['word'] if len(rect['word']) > 0 else u'/')  # a if a>b else c
                temp[str(i)] = t
            t = []
        df = pd.DataFrame(temp)
        df.to_excel(excelWriter, sheet_name=im)
        excelWriter.save()

