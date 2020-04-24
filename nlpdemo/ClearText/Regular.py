#coding:gbk
"""
DESC: 正则表达式的学习
prompt:coding in python3
"""
import re

# line =u'this is pathon 数据处理课程，这次课程很好，env is Anaconda4.4, 本次授课时间是2020年4月16日'
#
# rege_str1 = '^t.*'  #开头+任意次数
# rege_str2 = '.*(s+)'  #匹配有多少个s
# rege_str3 = '.*?([\u4E00-\u9FA5]+课)'  #提取含有课的中文字符串
#
#
# res = re.match(rege_str3,line)
# if res:
#     print(res.group(0))
# else:
#     print('this is null')

#日期的提取
line = '张三出生于1990年1月1日'
line2 = '李四出生于1990-10-1'
line3 = '王五出生于1990-10-10'
line4 = '孙刘出生于1990/10/3'
line5 = '王八出生于1990-10'

rege_str = '.*(\d{4}[年/-]\d{1,2}([月/-]\d{1,2}|[日]$|$))'
res = re.match(rege_str,line)
if res:
    print(res.group(0))
else:
    print('null')
# res2 = re.match(line2,rege_str).group(1)
# res3 = re.match(line3,rege_str).group(1)
# res4 = re.match(line4,rege_str).group(1)
# res5 = re.match(line5,rege_str).group(1)
#
# print(res)
# print(res2)
# print(res3)
# print(res4)
# print(res5)


