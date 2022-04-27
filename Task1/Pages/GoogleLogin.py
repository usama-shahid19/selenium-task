from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time





class GoogleLoginPage():


    email_textbox_element_id = "identifierId"
    emailpage_next_button_cssselector = "identifierNext"
    password_textbox_element_cssselector = "input[name='password']"

    def __init__(self, driver):
        self.driver = driver

        # self.email_textbox_element_id = "identifierId"
        # self.emailpage_next_button_cssselector = "identifierNext"
        # self.password_textbox_element_cssselector = "input[name='password']"


    def enter_email(self, email):
        self.driver.find_element_by_id(self.email_textbox_element_id).clear()
        self.driver.find_element_by_id(self.email_textbox_element_id).send_keys(email)
        self.driver.find_element_by_id(self.email_textbox_element_id).send_keys(Keys.RETURN)

    def enter_password(self, password):
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_css_selector(self.password_textbox_element_cssselector).clear()
        self.driver.find_element_by_css_selector(self.password_textbox_element_cssselector).send_keys(password)
        self.driver.find_element_by_css_selector(self.password_textbox_element_cssselector).send_keys(Keys.RETURN)


