
import time
import pytest


from selenium.webdriver.common.by import By
from PageObjects.LoginPage import Login
from utilities.readconfigfile import ReadValue
from utilities.Logger import LogGen
from utilities import XLutils

class Test_Login_DDT:
    Url = ReadValue.getUrl()
    log = LogGen.loggen()
    path= "C:\\Users\\DELL\\PycharmProjects\\Orangehrm Demo 1\\TestData\\LoginData.xlsx"

    def test_Login_ddt_004(self,setup):
        self.log.info("opening browser")
        self.driver = setup
        self.log.info("Going to Url")
        self.driver.get(self.Url)
        self.lp = Login(self.driver)
        self.rows = XLutils.getRowCount(self.path,'Sheet1')
        print("Number of rows are --->", self.rows)

        for r in range(2, self.rows+1):
            self.username = XLutils.readData(self.path,'Sheet1', r ,1)
            self.password = XLutils.readData(self.path, 'Sheet1', r, 2)
            self.exp_status = XLutils.readData(self.path, 'Sheet1', r, 3)

            self.lp.Enter_Username(self.username)
            self.log.info("Enter Username -->" + self.username)
            self.lp.Enter_Password(self.password)
            self.log.info("Enter Password -->" + self.password)
            self.lp.Click_Login()
            self.log.info("Clicked on Login Button")
            Login_status=[]
            if self.lp.Login_status() == True:

# If right username & password is given & login then testcase is passed
                if self.exp_status == "Pass":
                    Login_status.append("Pass")
                    self.driver.save_screenshot("C:\\Users\\DELL\\PycharmProjects\\Orangehrm Demo 1\\Screenshots\\test_login_ddt_004_Pass.png")
                    self.lp.Click_Menu_Button()
                    self.log.info("Click on Menu Button")
                    self.lp.Click_Logout_Button()
                    self.log.info("Click on Logout Button")
                    XLutils.writeData(self.path,'Sheet1',r,4,"Pass")

# If wrong username & password is given & still login then testcase is failed
                elif self.exp_status== "Fail":
                    Login_status.append("Fail")
                    self.driver.save_screenshot("C:\\Users\\DELL\\PycharmProjects\\Orangehrm Demo 1\\Screenshots\\test_login_ddt_004_Fail.png")
                    self.lp.Click_Menu_Button()
                    self.log.info("Click on Menu Button")
                    self.lp.Click_Logout_Button()
                    self.log.info("Click on Logout Button")
                    XLutils.writeData(self.path, 'Sheet1', r, 4, "Fail")

            else:

# If wrong username & password is given & not login then testcase is passed
                if self.exp_status == "Fail":
                    Login_status.append("Pass")
                    self.driver.save_screenshot("C:\\Users\\DELL\\PycharmProjects\\Orangehrm Demo 1\\Screenshots\\test_login_ddt_004_Pass.png")
                    XLutils.writeData(self.path, 'Sheet1', r, 4, "Fail")

# If right username & password is given & still not login then testcase is failed
                elif self.exp_status == "Pass":
                    Login_status.append("Fail")
                    self.driver.save_screenshot("C:\\Users\\DELL\\PycharmProjects\\Orangehrm Demo 1\\Screenshots\\test_login_ddt_004_Fail.png")
                    XLutils.writeData(self.path, 'Sheet1', r, 4, "Fail")
            print(Login_status)

        if "Fail" not in Login_status:
            self.log.info("test_login_ddt_004 is Passed")
            assert True
        else:
            self.log.info("test_login_ddt_004 is Failed")
            assert False
        self.driver.close()
        self.log.info("test_login_ddt_004 is completed")



