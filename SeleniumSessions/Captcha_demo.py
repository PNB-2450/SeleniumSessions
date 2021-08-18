import time

from captcha_solver import CaptchaSolver
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import captcha_solver

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get('https://cosmos.angelbroking.com/login/')
driver.find_element(By.XPATH, "//input[@id='id_email']").send_keys('nagendra@scaledesk.xyz')
driver.find_element(By.XPATH, "//input[@id='id_password']").send_keys("Test@12345")

frame = driver.find_element(By.XPATH, "//iframe[@title='reCAPTCHA']")
driver.switch_to.frame(frame)
print('It is Iframe')

#driver.find_element(By.XPATH, "//div[@class='recaptcha-checkbox-border']").click()

driver.execute_script('document.getElementById("rc-anchor-container").click()')
driver.switch_to.default_content()

driver.find_element(By.XPATH, "//button[@type='submit']//span[@class='btn-border']").click()