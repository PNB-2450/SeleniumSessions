import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)
driver.get("https://www.orangehrm.com/orangehrm-30-day-trial/")
print(driver.title)


url_filed = driver.find_element(By.ID, "Form_submitForm_subdomain")
first_name = driver.find_element(By.NAME, "FirstName")
last_name = driver.find_element(By.ID, "Form_submitForm_LastName")
email = driver.find_element(By.ID, "Form_submitForm_Email")

url_filed.send_keys("Nagendra abau")
first_name.send_keys("Chanti babu")
last_name.send_keys("Timothy")
email.send_keys("asfasd@gmail.com")




time.sleep(5)
driver.quit()