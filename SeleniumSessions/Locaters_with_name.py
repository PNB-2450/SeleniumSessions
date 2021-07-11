import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("https://classic.freecrm.com/")
print(driver.title)

username= driver.find_element(By.NAME, "username")
password = driver.find_element(By.NAME, "password")
login = driver.find_element(By.XPATH, "//input[@value='Login']")

username.send_keys("batchautomation")
password.send_keys("Test@12345")
login.click()