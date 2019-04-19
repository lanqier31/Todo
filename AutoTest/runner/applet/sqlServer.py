import pymssql
import pandas as pd
import json,re,urllib
import openpyxl


conn = pymssql.connect('192.168.10.164', 'sa', 'sa', '20190327')

cur = conn.cursor(as_dict=True)   #游标返回行为字典变量

sqltxt = "select a.HospitalNumber, b.ReportContent,c.ReportContent OldReportContent from Report_Check_Code a\
           inner join ReportManage b on a.ReportNo=b.ReportNo\
           inner join HospitalOriginalReportItem c on a.ReportNo=c.ReportNo\
           where a.ReportType= '超声声像' "

cur.execute(sqltxt)
data = cur.fetchall()
result={}
gs=[]
for row in data:
    try:
        result['HID']=row['HospitalNumber']
        # print (row['OldReportContent'].replace('\n',''))

        result['suoj_yuanshi']= re.search(r'(?<=\<checkResult\>).*?(?=\<\/checkResult\>)', row['OldReportContent'].replace('\n','')).group()
        result['zhend_yuanshi']= re.search(r'(?<=\<checkConclusion\>).*?(?=\<\/checkConclusion\>)', row['OldReportContent'].replace('\n','')).group()

        result['suoj_yuanshi'] = re.search(r'(?<=\<!\[CDATA\[).*?(?=\]\]\>)', result['suoj_yuanshi']).group()
        result['zhend_yuanshi'] = re.search(r'(?<=\<!\[CDATA\[).*?(?=\]\]\>)', result['zhend_yuanshi']).group()

        result['suoj_fo'] = urllib.parse.unquote(json.loads(row['ReportContent'])['checkResult'])
        # result['suoj_fo'] = urllib.parse.unquote(result['suoj_fo'])
        result['suoj_ln'] = urllib.parse.unquote(json.loads(row['ReportContent'])['checkResult2'])
        # result['suoj_ln'] = urllib.parse.unquote(result['suoj_ln'])
        result['zhend_fo']= urllib.parse.unquote(json.loads(row['ReportContent'])['checkConclusion'])
        # result['zhend_fo'] = urllib.parse.unquote(result['zhend_fo'])
        result['zhend_ln']= urllib.parse.unquote(json.loads(row['ReportContent'])['checkConclusion2'])
        # result['zhend_ln'] = urllib.parse.unquote(result['zhend_ln'])
        gs.append(result)
        result = {}
    except Exception:
        print (Exception,result['HID'])
df = pd.DataFrame(gs)
writer = pd.ExcelWriter('Bchao.xlsx')
df.to_excel(writer,'sheet1')
writer.save()
conn.close()
