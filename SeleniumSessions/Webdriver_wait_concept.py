import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.chrome import ChromeDriverManager

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.freshworks.com/')

wait= WebDriverWait(driver, 10)
footer_list = wait.until(ec.presence_of_all_elements_located((By.XPATH,"//ul[@class='footer-nav']/li")))
print(len(footer_list))

for ele in footer_list:
    print(ele.text)


driver.quit()