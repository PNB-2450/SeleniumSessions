from selenium import webdriver
from selenium.webdriver.common.alert import Alert


# driveer = webdriver.Chrome(executable_path="D:\\PyCharm\\chromedriver.exe")
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("")
title = driver.title
currentURl = driver.current_url
print(title)
print(currentURl)
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("")
driver.back()
driver.forward()
driver.refresh()
driver.close()
driver.quit()
Alert(driver).accept()
Alert(driver).dismiss()
Alert(driver).send_keys('Alert text')
Alert(driver).text

driver.close()
driver.quit()
