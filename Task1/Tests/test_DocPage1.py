from Pages.DocPage1 import DocPagefirst
from Tests.test_GoogleLogin import Test_001_Login
from selenium import webdriver
#from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

class Test_002_EnterDataPage1():

    baseURL = "https://docs.google.com/forms/d/e/1FAIpQLSfSGh4qzssK1gnZ6JEUe1D4E3lmGCelVD0VZgdHs_y7K_U7rA/viewform"
    phoneNo = "03411222121"
    name = "Usama Shahid"
    email = "hellotestselenium@gmail.com"
    cnic = "3630222103157"
    googleemail = "hellotestselenium@gmail.com"
    googlepassword = "selenium121"
    accepted_emails = ["hellotestselenium @ gmail.com", "testing @ anything.com"]

    def test_docPage1(self):
        self.driver = webdriver.Chrome(executable_path="/Users/usamashahid/PycharmProjects/Task1/Driver/chromedriver")
        self.driver.get(self.baseURL)
        self.dp = DocPagefirst(self.driver)
        self.dp.enter_email(self.googleemail)
        self.dp.driver.implicitly_wait(10)
        self.dp.enter_password(self.googlepassword)
        self.dp.driver.implicitly_wait(10)
        #self.dp.clearallfields()
        #self.dp.clickClearform()
        self.dp.clickNext()
        self.dp.erromessagedisplayed()
        self.dp.enterPnoneNo(self.phoneNo)
        self.dp.enter_email(self.email)

        if self.email in self.accepted_emails:
            return True
        else:
            return False
        self.dp.enterNameOfPerson(self.name)
        self.dp.enterCnic(self.cnic)
        assert len(self.cnic) == 16




        self.dp.clickNext()



        # if self.dp.erromessagedisplayed():
        #     assert True
        # else:
        #     assert False