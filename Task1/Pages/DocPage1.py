from selenium import webdriver
from Pages.GoogleLogin import GoogleLoginPage

class DocPagefirst(GoogleLoginPage):

    phone_no_css_selector = "div[data-params*='Phone Number'] input[type = 'text']"
    name_css_selector = "div [data-params*= 'Name'] input[type= 'text']"
    email_css_selector = "div [data-params*= 'Email'] input[type= 'email']"
    cnic_css_selector = "div [data-params*= 'CNIC'] input[type= 'text']"
    next_button_css_selector = "div [role = 'button']"
    errorMessage_css = "div [role ='alert']"
    clear_button_xpath = "//span [contains(text(),'Clear form')]"
    clear_button_on_popup_css = "body > div:nth-child(13) > div:nth-child(1) > div:nth-child(2) > div:nth-child(4) > div:nth-child(2) > span:nth-child(3) > span:nth-child(1)"

    def __init__(self, driver):
        self.driver = driver

    def clearallfields(self):
        self.driver.find_element_by_css_selector(self.phone_no_css_selector).clear()
        self.driver.find_element_by_css_selector(self.name_css_selector).clear()
        self.driver.find_element_by_css_selector(self.email_css_selector).clear()
        self.driver.find_element_by_css_selector(self.cnic_css_selector).clear()

    def enterPnoneNo(self, phoneNo):
        self.driver.find_element_by_css_selector(self.phone_no_css_selector).clear()
        self.driver.find_element_by_css_selector(self.phone_no_css_selector).click()
        self.driver.find_element_by_css_selector(self.phone_no_css_selector).send_keys(phoneNo)


    def enterNameOfPerson(self, name):
        self.driver.find_element_by_css_selector(self.name_css_selector).clear()
        self.driver.find_element_by_css_selector(self.name_css_selector).click()
        self.driver.find_element_by_css_selector(self.name_css_selector).send_keys(name)

    def enterEmail(self, emailId):
        self.driver.find_element_by_css_selector(self.email_css_selector).clear()
        self.driver.find_element_by_css_selector(self.email_css_selector).click()
        self.driver.find_element_by_css_selector(self.email_css_selector).send_keys(emailId)

    def enterCnic(self, cnic):
        self.driver.find_element_by_css_selector(self.cnic_css_selector).clear()
        self.driver.find_element_by_css_selector(self.cnic_css_selector).click()
        self.driver.find_element_by_css_selector(self.cnic_css_selector).send_keys(cnic)


    def clickNext(self):
        self.driver.find_element_by_css_selector(self.next_button_css_selector).click()

    def clickClearform(self):
        self.driver.find_element_by_xpath(self.clear_button_xpath).click()
        self.driver.find_element_by_css_selector(self.clear_button_on_popup_css).click()

    def erromessagedisplayed(self):
        if self.driver.find_element_by_css_selector(self.errorMessage_css).is_displayed():
            return True
        else:
            return False