import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.chrome import ChromeDriverManager

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://smartbuzz.angelbroking.com/')

print(driver.title)

wait = WebDriverWait(driver, 10)
readNews_ele = wait.until(ec.element_to_be_clickable((By.LINK_TEXT, "Read News")))
print(readNews_ele.text)
readNews_ele.click()

driver.back()

demat_name =wait.until(ec.visibility_of_element_located((By.ID, "demat-name")))
demat_name.send_keys('Nagendra Babu')

driver.quit()