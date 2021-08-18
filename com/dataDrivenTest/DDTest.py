from selenium.webdriver.common.alert import Alert

import XL_Utils
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='D:\PyCharm\chromedriver.exe')
driver.implicitly_wait(5)

driver.get("http://automationpractice.com/")
driver.find_element(By.XPATH,"//a[@title='Log in to your customer account']").click()
driver.maximize_window()
path ="D:\Testdata.xlsx"
row = XL_Utils.getRowCount(path,"Data")
for r in range(2,row+1):
    username = XL_Utils.readData(path,"Data",r,1)
    password = XL_Utils.readData(path,"Data", r,2)

    ele1=driver.find_element(By.XPATH,"//input[@id='email']")
    ele1.clear()
    ele1.send_keys(username)

    ele2 = driver.find_element(By.XPATH, "//input[@type='password']")
    ele2.clear()
    ele2.send_keys(password)

    driver.find_element(By.XPATH, "//button[@id='SubmitLogin']").click()

    if driver.title == "My account - My Store":
        print("Test case is passed")
        XL_Utils.writeData(path,"Data",r,3,'Passed')
    else:
        print('Testcase is failed')
        XL_Utils.writeData(path,"Data",r,3,'Failed')


driver.quit()