from Pages.GoogleLogin import GoogleLoginPage
from selenium import webdriver
#from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

class Test_001_Login():

    baseURL = "https://docs.google.com/forms/d/e/1FAIpQLSfSGh4qzssK1gnZ6JEUe1D4E3lmGCelVD0VZgdHs_y7K_U7rA/viewform"
    email = "hellotestselenium@gmail.com"
    password = "selenium121"


    def test_logintoGoogle(self):
        self.driver = webdriver.Chrome(executable_path="/Users/usamashahid/PycharmProjects/Task1/Driver/chromedriver")
        self.driver.get(self.baseURL)
        self.glp = GoogleLoginPage(self.driver)
        self.glp.enter_email(self.email)
        self.glp.driver.implicitly_wait(10)
        self.glp.enter_password(self.password)
        # act_title = self.driver.title
        # self.driver.implicitly_wait(7)
        # if act_title == "Automation Assessment":
        #     assert True
        # else:
        #     assert False