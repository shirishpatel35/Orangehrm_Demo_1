
import time
import pytest


from selenium.webdriver.common.by import By
from PageObjects.LoginPage import Login
from utilities.readconfigfile import ReadValue
from utilities.Logger import LogGen

class Test_Url_Login:
    Url = ReadValue.getUrl()
    log = LogGen.loggen()


    def test_Login_Params_003(self,setup,getDataForLogin):
        self.log.info("opening browser")
        self.driver = setup
        self.log.info("Going to Url")
        self.driver.get(self.Url)
        self.lp = Login(self.driver)
        self.lp.Enter_Username(getDataForLogin[0])
        self.log.info("Enter Username -->" + getDataForLogin[0])
        self.lp.Enter_Password(getDataForLogin[1])
        self.log.info("Enter Password -->" + getDataForLogin[1])
        self.lp.Click_Login()
        self.log.info("Clicked on Login Button")
        Login_status=[]
        if self.lp.Login_status() == True:

# If right username & password is given & login then testcase is passed
            if getDataForLogin[2]== "Pass":
                Login_status.append("Pass")
                self.driver.save_screenshot("C:\\Users\\DELL\\PycharmProjects\\Orangehrm Demo 1\\Screenshots\\test_login_params_003_Pass.png")
                self.lp.Click_Menu_Button()
                self.log.info("Click on Menu Button")
                self.lp.Click_Logout_Button()
                self.log.info("Click on Logout Button")

# If wrong username & password is given & still login then testcase is failed
            elif getDataForLogin[2]== "Fail":
                Login_status.append("Fail")
                self.driver.save_screenshot("C:\\Users\\DELL\\PycharmProjects\\Orangehrm Demo 1\\Screenshots\\test_login_params_003_Fail.png")
                self.lp.Click_Menu_Button()
                self.log.info("Click on Menu Button")
                self.lp.Click_Logout_Button()
                self.log.info("Click on Logout Button")

        else:

# If wrong username & password is given & not login then testcase is passed
            if getDataForLogin[2] == "Fail":
                Login_status.append("Pass")
                self.driver.save_screenshot("C:\\Users\\DELL\\PycharmProjects\\Orangehrm Demo 1\\Screenshots\\test_login_params_003_Pass.png")

# If right username & password is given & still not login then testcase is failed
            elif getDataForLogin[2] == "Pass":
                Login_status.append("Fail")
                self.driver.save_screenshot("C:\\Users\\DELL\\PycharmProjects\\Orangehrm Demo 1\\Screenshots\\test_login_params_003_Fail.png")
        print(Login_status)

        if "Fail" not in Login_status:
            self.log.info("test_login_params_003 is Passed")
            assert True
        else:
            self.log.info("test_login_params_003 is Failed")
            assert False
        self.driver.close()
        self.log.info("test_login_params_003 is completed")



