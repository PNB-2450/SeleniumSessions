import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(7)
driver.get('https://cgi-lib.berkeley.edu/ex/fup.html')

# type = 'file' attribute should be there

driver.find_element(By.NAME,"upfile").send_keys('C:/Users/pnb98/Desktop/Python.txt')
driver.find_element(By.XPATH,"//input[@type='submit']").click()

print(driver.title)
time.sleep(3)
driver.quit()