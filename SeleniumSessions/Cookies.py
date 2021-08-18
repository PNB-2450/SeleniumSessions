import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(7)
driver.get('https://www.rediff.com/')

print(driver.get_cookies())

driver.add_cookie({"name":"ChantiPython", "domain":"rediff.com", "value":'Nagendravalue'})
cookies1 = driver.get_cookies()
for cook in cookies1:
    print(cook)






driver.quit()