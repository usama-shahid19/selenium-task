import pytest
from selenium import webdriver

@pytest.fixture()
def setup():
    driver = webdriver.Chrome(executable_path="/Users/usamashahid/PycharmProjects/Task1/Driver/chromedriver")
    return driver