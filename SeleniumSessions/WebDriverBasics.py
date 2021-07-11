import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='D:\\PyCharm\\chromedriver.exe')
driver.implicitly_wait(5)
driver.get('https://www.google.com/')
driver.maximize_window()
print(driver.title)


driver.find_element(By.NAME,'q').send_keys('Python ')

optionList = driver.find_elements(By.XPATH,"//ul[@class='erkvQe']/li")
for list in optionList:
    print(list.text)
    if list.text == 'python programming':
        list.click()
        break

time.sleep(5)
driver.quit()
