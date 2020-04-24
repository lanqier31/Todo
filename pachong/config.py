# Author：WeirGao

import os, sys

basedir = os.path.abspath(os.path.dirname(os.getcwd()))
log_file_path = os.path.join(basedir, 'log')
url={
    "浙江政府采购网":"http://search.ccgp.gov.cn/bxsearch",
    "中国政府采购网":"http://www.ccgp.gov.cn/"
}
keywords=['医疗保障信息平台','卫生计生信息中心','健康信息','电子病历']
reservedwords = ['项目编号：','项目名称：','采购单位名称：','成交日期：','成交供应商：','成交价格：']
labelWords = ['项目编号：','项目名称：','采购单位名称：','成交日期：','成交供应商：','成交价格：']

related = {
     '项目编号':'项目编号：',
     '项目名称':'项目名称：',
     '采购单位':'采购单位名称：|中标供应商名称',
     '中标日期':'成交日期：',
     '中标供应商':'成交供应商：',
     '成交价格':'成交价格：|中标金额：|',
         }


