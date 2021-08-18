import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def select_multi_values(options_list, values):
    for ele in options_list:
        print(ele.text)
        for k in range(len(values)):
            if ele.text == values[k]:
                ele.click()
                break






driver=webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/")

time.sleep(3)
driver.find_element(By.ID,'justAnInputBox').click()

time.sleep(3)
multi_list = driver.find_elements(By.CSS_SELECTOR,"span.comboTreeItemTitle")
value_list=['choice 2', 'choice 3', 'choice 6 2 1']
select_multi_values(multi_list, value_list)