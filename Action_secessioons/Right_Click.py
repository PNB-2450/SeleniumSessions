import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)

driver.get("http://swisnl.github.io/jQuery-contextMenu/demo.html")
driver.maximize_window()

""" Right / Context Click """

right_click = driver.find_element(By.XPATH, "//span[text()='right click me']")

actchain = ActionChains(driver)
actchain.context_click(right_click).perform()

option_list = driver.find_element(By.XPATH, "//ul[@Class='context-menu-list context-menu-root']/li/span")

for ele in option_list:
    print(ele.text)
    if ele.text == 'Copy':
        ele.click()
        break


driver.quit()