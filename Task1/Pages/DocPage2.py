from Pages.DocPage1 import DocPagefirst


class DocPagesecond(DocPagefirst):

    firebug_selection_css_selector = "label[for='i8']"
    locator_type_css_selector = "label[for='i21']"
    next_btn_css_selector = "body div[class='Uc2NEf'] div[class='teQAzf'] form[id='mG61Hd'] div[class='RH5hzf RLS9Fe'] div[class='lrKTG'] div[class='ThHDze'] div[class='DE3NNc CekdCb'] div[class='lRwqcd'] div:nth-child(1) span:nth-child(1)"


    def __init__(self, driver):
        self.driver = driver

    def select_firefbug_option(self):
        self.driver.find_element_by_css_selector(self.firebug_selection_css_selector).click()

    def type_of_locator(self):
        self.driver.find_element_by_css_selector(self.locator_type_css_selector).click()

    def clickNext(self):
        self.driver.find_element_by_css_selector(self.next_btn_css_selector).click()
