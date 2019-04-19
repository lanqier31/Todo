# Author：WeirGao

import os, sys

browserType = 'Chrome'
IP = '192.168.10.243/'
Version = 'syf1.2.0'
LoginUrl= 'http://'+IP+Version+'/login/index'
baseUrl = 'http://192.168.10.243/'
basedir = os.path.abspath(os.path.dirname(os.getcwd()))
log_file_path = os.path.join(basedir, 'log')
chromedriver_path = os.path.join(basedir, 'config/drivers/chromedriver.exe')
screens_file_path = os.path.join(basedir, 'result/PageScreen')
autoCase_path = os.path.join(basedir, 'testData\AutoTestCases.xlsx')

reportType={
    "Bchao_pre": "超声声像",
    "Bchao_fellowup": "超声声像",
    "pathology": "常规病理",
    "pathology_bingdong": "冰冻标本",
    "ImgA": "影像A",
    "ImgB": "影像B",
    "Img131I": "核素影像",
    "AsssyA": "检验A",
    "BFna_cell": "细胞病理",
    "B_FNA":"B-FNA操作",
}
