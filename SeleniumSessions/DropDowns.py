from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("https://www.seleniumeasy.com/test/basic-select-dropdown-demo.html")
driver.maximize_window()
driver.find_element(By.ID,'select-demo').click()

def select_values(element, value):
    dd = Select(element)
    dd.select_by_value(value)


def select_values_from_dropdown(elementList, value):
    for ele in elementList:
        print(ele.text)
        if ele.text == value:
            ele.click()
            break

a = driver.find_elements(By.XPATH, "//Select[@id='select=demo']/option")
#select_values(a, 'Tuesday')
select_values_from_dropdown(a,"Monday")