from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd
import os,time
import config
from demo import getData

data=[]
options = Options()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
# options.add_argument('--headless')
options.add_argument("--start-maximized")  # 默认屏幕最大化
options.add_argument('disable-infobars')  # 规避浏览器显示 Chrome正在受到自动软件的控制
# options.add_argument(r"user-data-dir=C:\Users\dell\AppData\Local\Google\Chrome\User Data")  # 读取用户设置内容
driver = webdriver.Chrome(chrome_options=options)
url=config.url['中国政府采购网']
keyword = config.keywords[0]
driver.get(url)
driver.find_element_by_id('kw').clear()
driver.find_element_by_id('kw').send_keys(keyword)
driver.find_element_by_id('doSearch2').click()
time.sleep(1)
ul = driver.find_element_by_class_name('vT-srch-result-list-bid')
lis = ul.find_elements_by_tag_name('li')
for li in lis:
    li.find_element_by_tag_name('a').click()
    windows = driver.window_handles    # 获取打开的多个窗口句柄
    driver.switch_to.window(windows[-1])  # 切换到当前最新打开的窗口
    print(driver.current_url)
    driver.find_element_by_id('displayGG').click()
    data .append(getData(driver.current_url))
    driver.close()
    driver.switch_to.window(windows[0])
    print (driver.window_handles)
df = pd.DataFrame(data).loc[:, config.reservedwords]
writer = pd.ExcelWriter('demo2.xlsx')
df.to_excel(writer, 'sheet1')
writer.save()



