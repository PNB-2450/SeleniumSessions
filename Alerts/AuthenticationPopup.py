import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(7)
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")

time.sleep(3)
driver.quit()
