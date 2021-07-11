import time

import webdriver_manager
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


browserName = "chrome"

if browserName == 'chrome':
    driver = webdriver.Chrome(ChromeDriverManager().install())
elif browserName == "firefox":
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
else:
    print('Enter valid browser name')

driver.implicitly_wait(20)
driver.get('https://selenium-python.readthedocs.io/')
driver.maximize_window()
print(driver.title)


#driver.find_element(By.CLASS_NAME, 'homepage-nav-login').click()


