import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def select_all_values(options_list, value):
    if not value[0] == 'all':
        for ele in options_list:
            print(ele.text)
            for k in range(len(value)):
                if ele.text == value[k]:
                    ele.click()
                    break
    else:
        try:
            for ele in options_list:
                ele.click()
        except Exception as e:
            print(e)


driver=webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/")

time.sleep(3)
driver.find_element(By.ID,'justAnInputBox').click()

time.sleep(3)
drop_list = driver.find_elements(By.CSS_SELECTOR,"span.comboTreeItemTitle")
value_list = ['all']
select_all_values(drop_list, value_list)
