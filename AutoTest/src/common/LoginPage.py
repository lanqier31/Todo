from src.common.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time

class LoginPage(BasePage):

    username = (By.ID,'txtUserName')
    password = (By.ID,'txtPassword')
    loginbtn = (By.ID,'btnConfirm')
    loginAlert = (By.ID,'spanMessage')
    allLink = (By.ID,'allLink')

    #点击登陆图标
    def click_loginbtn(self):
        loginbtn=self.driver.find_element(*LoginPage.loginbtn)
        loginbtn.click()

    #重置用户名
    def reset_loginname(self,name):
        WebDriverWait(self.driver, 10).until(lambda the_driver: the_driver.find_element(*LoginPage.username).is_displayed())
        loginName = self.driver.find_element(*LoginPage.username)
        try:

            ActionChains(self.driver).move_to_element(loginName).perform()
            loginName.click()
            loginName.clear()  # 调用clear()方法去清除
        except Exception as e:
            print ("Exception found", format(e))
        loginName.send_keys(name)

    #重置密码
    def reset_password(self,pwd):
        WebDriverWait(self.driver, 10).until(lambda the_driver: the_driver.find_element(*LoginPage.password).is_displayed())
        self.driver.find_element(*LoginPage.password).clear()
        self.driver.find_element(*LoginPage.password).send_keys(pwd)

    # 登陆Syf系统
    def login_syf(self,url, name, passwd):
        self.driver.get(url)
        WebDriverWait(self.driver, 10).until(lambda the_driver: the_driver.find_element(*LoginPage.loginbtn).is_displayed())
        self.reset_loginname(name)
        self.reset_password(passwd)
        self.click_loginbtn()
        time.sleep(3)
        # WebDriverWait(self.driver, 10).until(lambda the_driver: the_driver.find_element(*LoginPage.allLink).is_displayed())
        if 'Login/SelectSystem' in self.driver.current_url:
            return 'Login Success, test login is pass'
        else:
            return 'Login failed!'
