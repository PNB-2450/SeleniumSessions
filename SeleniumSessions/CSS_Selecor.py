import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(20)
driver.get("https://app.hubspot.com/login")
print(driver.title)
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR, "#username").send_keys("nagendr@gmail.com")
driver.find_elememt(By.CSS_SELECTOR, "input#password").send_keys('Test@12345')
driver.find_element(By.CSS_SELECTOR, "#loginBtn").click()
driver.minimize_window()