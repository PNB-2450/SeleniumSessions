import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager



driver = None
@pytest.fixture(scope="module")
def init_driver():
    global driver
    print("_______________________setup_______________________")
    driver=webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.delete_all_cookies()
    driver.get('https://www.google.com')

    yield
    print("_______________________tear down_______________________")
    driver.quit()



def test_title(init_driver):
    assert driver.title=="Google"

def test_url(init_driver):
    assert driver.current_url=="https://www.google.com/"



