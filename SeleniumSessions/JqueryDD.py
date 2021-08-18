import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def select_values(options_list, value):
    for ele in dd_list:
        print(ele.text)
        if ele.text == value:
            ele.click()
            break


driver=webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/")
time.sleep(3)
driver.find_element(By.ID, "justAnInputBox").click()
time.sleep(3)
dd_list = driver.find_elements(By.CSS_SELECTOR, "span.comboTreeItemTitle")
select_values(dd_list, 'choice 2 1')