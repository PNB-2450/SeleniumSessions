import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager



driver = None

def setup_module(module):
    global driver
    driver=webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.delete_all_cookies()
    driver.get('https://www.google.com')


def teardown_module(module):
    driver.quit()



def test_title():
    assert driver.title=="Google"

def test_url():
    assert driver.current_url=="www.gmail.com"



