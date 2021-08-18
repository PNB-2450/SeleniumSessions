import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.chrome import ChromeDriverManager

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.amazon.in/')

wait = WebDriverWait(driver, 10)
# wait.until(ec.title_is('HubSpot Login'))
wait.until(ec.title_contains('Online Shopping site'))
print(driver.title)

search = wait.until(ec.presence_of_element_located((By.ID, 'twotabsearchtextbox')))
search.send_keys('test@gmail.com')


time.sleep(3)
driver.quit()

