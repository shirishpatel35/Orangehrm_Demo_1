
# Scenario 1:(Before Creating Page Object for Login)

# import time
#
# from selenium import webdriver
# from selenium.common import NoSuchElementException
# from selenium.webdriver.common.by import By
#
#
# class Test_Url_Login:
#
#     def test_Url_001(self):
#         driver=webdriver.Chrome()
#         driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
#         time.sleep(3)
#         if driver.title=='OrangeHRM':
#             assert True
#         else:
#             assert False
#
#     def test_Login_002(self):
#         driver=webdriver.Chrome()
#         driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
#         time.sleep(3)
#         driver.find_element(By.NAME,'username').send_keys("Admin")
#         driver.find_element(By.NAME,'password').send_keys("admin123")
#         driver.find_element(By.XPATH,"//button[normalize-space()='Login']").click()
#         time.sleep(3)
#
#         def login_status():
#             try:
#                 driver.find_element(By.XPATH,"//li[@class='oxd-userdropdown']").click()
#                 return True
#             except NoSuchElementException:
#                 return False
#
#         if login_status() == True:
#             driver.find_element(By.CLASS_NAME, 'oxd-userdropdown-name').click()
#             driver.find_element(By.XPATH,"//a[normalize-space()='Logout']").click()
#             assert True
#         else:
#             assert False


#-----------------------------------------------------------------------

# Scenario 2:(After Creating Page Object for Login)

import time
import pytest


from selenium.webdriver.common.by import By
from PageObjects.LoginPage import Login
from utilities.readconfigfile import ReadValue
from utilities.Logger import LogGen


class Test_Url_Login:
    username = ReadValue.getUsername()
    password = ReadValue.getPassword()
    Url = ReadValue.getUrl()
    log = LogGen.loggen()

    def test_Url_001(self,setup):
        self.log.info("opening browser")
        self.driver = setup
        self.log.info("Going to Url")
        self.driver.get(self.Url)
        self.log.info("Checking Page title")
        if self.driver.title=='OrangeHRM':
            self.log.info("test_Url_001 is passed")
            self.driver.save_screenshot("C:\\Users\\DELL\\PycharmProjects\\Orangehrm_Demo_1\\Screenshots\\test_url_001_pass.png")
            assert True
        else:
            self.log.info("test_Url_001 is failed")
            self.driver.save_screenshot("C:\\Users\\DELL\\PycharmProjects\\Orangehrm_Demo_1\\Screenshots\\test_url_001_fail.png")
            assert False
        self.driver.close()
        self.log.info("test_Url_001 is completed")


    def test_Login_002(self,setup):
        self.log.info("opening browser")
        self.driver = setup
        self.log.info("Going to Url")
        self.driver.get(self.Url)
        self.lp = Login(self.driver)
        self.lp.Enter_Username(self.username)
        self.lp.Enter_Password(self.password)
        self.lp.Click_Login()
        self.log.info("Clicked on Login Button")
        if self.lp.Login_status() == True:
            self.log.info("test_Login_002 is passed")
            self.driver.save_screenshot("C:\\Users\\DELL\\PycharmProjects\\Orangehrm_Demo_1\\Screenshots\\test_login_002_pass.png")
            self.lp.Click_Menu_Button()
            self.lp.Click_Logout_Button()
            assert True
        else:
            self.log.info("test_Login_002 is failed")
            self.driver.save_screenshot("C:\\Users\\DELL\\PycharmProjects\\Orangehrm_Demo_1\\Screenshots\\test_login_002_fail.png")
            assert False
        self.driver.close()
        self.log.info("test_Login_002 is completed")


