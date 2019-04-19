from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import sys,os,time
from config import baseconf
from selenium.webdriver.support.ui import WebDriverWait


class BasePage(object):

    def __init__(self):
        browser = baseconf.browserType
        # url = baseconf.LoginUrl
        if browser == "Firefox":
            self.driver = webdriver.Firefox()
        elif browser == "Chrome":
            self.path = baseconf.chromedriver_path
            self.options = Options()
            # self.options.add_argument('--headless')   #浏览器不提供可视化页面
            self.options.add_argument("--start-maximized")  # 默认屏幕最大化
            # self.options.add_argument("--no-sandbox")
            # self.options.add_argument("--disable-dev-shm-usage")
            # self.options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
            self.options.add_argument('disable-infobars')  # 规避浏览器显示 Chrome正在受到自动软件的控制
            self.options.add_argument(
                            r"user-data-dir=C:\Users\dell\AppData\Local\Google\Chrome\User Data")  # 读取用户设置内容

            self.driver = webdriver.Chrome(chrome_options=self.options)
        # self.driver.set_window_size(1920, 1080)
        # self.driver.maximize_window()
        # self.driver.get(url)


    # open url
    def open_url(self,url):
        self.driver.get(url)

    # close browser
    def quit_browser(self):
        self.driver.quit()

    def forward(self):
        self.driver.forward()

    def back(self):
        self.driver.back()

    def wait(self, seconds):
        self.driver.implicitly_wait(seconds)

    def alert_close(self):
        """判断是否存在提醒框并关闭"""
        waitAlert = WebDriverWait(self.driver, 10).until(EC.alert_is_present()(self.driver))
        if waitAlert:
            alert = EC.alert_is_present()(self.driver)
            if (u'外院手术' in alert.text):
                alert.dismiss()
            elif (u'没有此病人信息'in alert.text):
                alert.accept()
                log.Logger()
                return "不存在该病历号"
            elif u'没有抓取到报告内容'in alert.text:
                alert.accept()

            else:
                alert.accept()

    def screenPage(self,reportType):
        """
        截图功能；
        reportType:包含config 中 reporttype的key"""

        nowTime = time.strftime("%Y%m%d.%H.%M.%S")
        dirs = r'../PageScreen/' + reportType
        if not os.path.exists(dirs):
            os.makedirs(dirs)
        self.driver.get_screenshot_as_file(dirs + '/%s.png' % nowTime)

    def wait_loading(self):
        """waiting for divBlockHid disappear"""
        WebDriverWait(self.driver, 30,0.5).until_not(
            lambda the_driver: the_driver.find_element_by_class_name('divBlockHid').is_displayed())

    def wait(self,element):

        WebDriverWait(self.driver,30,0.5).until_not(
            lambda the_driver: the_driver.find_element(element).is_displayed())

    def goto_Report(self):

        url = 'http://' + baseconf.IP + baseconf.Version + '/SyfHospitalClinicalDataCenter/QueryReport?type=add&editmark=true'
        self.driver.get(url)