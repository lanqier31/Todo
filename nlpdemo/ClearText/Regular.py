#coding:gbk
"""
DESC: ������ʽ��ѧϰ
prompt:coding in python3
"""
import re

# line =u'this is pathon ���ݴ���γ̣���ογ̺ܺã�env is Anaconda4.4, �����ڿ�ʱ����2020��4��16��'
#
# rege_str1 = '^t.*'  #��ͷ+�������
# rege_str2 = '.*(s+)'  #ƥ���ж��ٸ�s
# rege_str3 = '.*?([\u4E00-\u9FA5]+��)'  #��ȡ���пε������ַ���
#
#
# res = re.match(rege_str3,line)
# if res:
#     print(res.group(0))
# else:
#     print('this is null')

#���ڵ���ȡ
line = '����������1990��1��1��'
line2 = '���ĳ�����1990-10-1'
line3 = '���������1990-10-10'
line4 = '����������1990/10/3'
line5 = '���˳�����1990-10'

rege_str = '.*(\d{4}[��/-]\d{1,2}([��/-]\d{1,2}|[��]$|$))'
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


