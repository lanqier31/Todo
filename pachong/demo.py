from bs4 import BeautifulSoup
from lxml import html
import xml
import requests

import config


def getData(url):

   # url = "http://www.ccgp.gov.cn/cggg/dfgg/cjgg/201906/t20190618_12282732.htm"
   f = requests.get(url)                 #Get该网页从而获取该html内容
   soup = BeautifulSoup(f.content, "lxml")  #用lxml解析器解析该网页的内容, 好像f.text也是返回的html
   #print(f.content.decode())
   #content = soup.find_all('div',class_="vF_detail_content" )   #因为calss和关键字冲突，所以改名class_
   temp={}
   data=[]
   for k in soup.find_all('div',class_='vF_detail_content'):#,找到div并且class为pl2的标签
      a = k.find_all('p')       #在每个对应div标签下找span标签，会发现，一个a里面有四组span
      for p in a:
         if p.text:
            for res in config.reservedwords:
               if res in p.text:
                  temp[res]=p.text.split("：")[-1]
      data.append(temp)
      return (data)

