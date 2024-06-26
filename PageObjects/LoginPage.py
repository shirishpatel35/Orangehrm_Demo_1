from selenium import webdriver
from selenium.common import NoSuchElementException,TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Login:
    text_username_Name = (By.NAME,'username')
    text_password_Name = (By.NAME, 'password')
    click_login_xpath = (By.XPATH,"//button[@type='submit']")
    click_menu_xpath = (By.XPATH,"//li[@class='oxd-userdropdown']")
    click_logout_xpath = (By.XPATH,"//a[normalize-space()='Logout']")

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,5)

    def Enter_Username(self,username):
        self.wait.until(expected_conditions.presence_of_element_located(self.text_username_Name))
        self.driver.find_element(*Login.text_username_Name).send_keys(username)

    def Enter_Password(self,password):
        self.driver.find_element(*Login.text_password_Name).send_keys(password)

    def Click_Login(self):
        self.driver.find_element(*Login.click_login_xpath).click()

    def Login_status(self):
        try:
            self.wait.until(expected_conditions.presence_of_element_located(self.click_menu_xpath))
            self.driver.find_element(*Login.click_menu_xpath)
            return True
        except (NoSuchElementException,TimeoutException):
            return False

    def Click_Menu_Button(self):
        self.wait.until(expected_conditions.presence_of_element_located(self.click_menu_xpath))
        self.driver.find_element(*Login.click_menu_xpath).click()

    def Click_Logout_Button(self):
        self.driver.find_element(*Login.click_logout_xpath).click()



