import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get('https://smartmoney.angelbroking.com/login/')

reg = driver.find_element(By.CLASS_NAME, "nav-item mx-xl-2 pt-0")
driver.execute_script("arguments[0].click();", reg)



# # Get the title through Java Script executor
# title = driver.execute_script("return document.title;")
# print(title)
#
# # Click on element using Java Script Executor
# amazon_pay = driver.find_element(By.LINK_TEXT,'Amazon Pay')
# driver.execute_script("arguments[0].click();", amazon_pay)
#
# # To get innerText from the particular  page
# innter_text = driver.execute_script("return document.documentElement.innerText;")
# print(innter_text)
#
#
# # To generate alert on web page
# #driver.execute_script("alert('Hello Selenium');")
#
#
# # To refresh the page
# driver.execute_script("history.go(0);")
#
# donate= driver.find_element(By.LINK_TEXT,'Donate')
# driver.execute_script("arguments[0].style.border= '3px solid red'", donate)













time.sleep(3)
#driver.quit()