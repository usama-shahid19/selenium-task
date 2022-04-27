from Tests.test_DocPage1 import Test_002_EnterDataPage1
from Pages.DocPage2 import DocPagesecond
from selenium import webdriver


class Test_003_Selectradiobuttons():

    baseURL = "https://docs.google.com/forms/d/e/1FAIpQLSfSGh4qzssK1gnZ6JEUe1D4E3lmGCelVD0VZgdHs_y7K_U7rA/viewform"

    def test_docPage2(self):
        self.testdocpage1con = Test_002_EnterDataPage1()
        self.testdocpage1con.test_docPage1()

        self.docPage1 = DocPagesecond()
        self.docPage1.firebug_selection_css_selector()
        self.docPage1.type_of_locator()
        self.docPage1.clickNext()
