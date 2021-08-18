import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)

driver.get("http://demo.automationtesting.in/Static.html")
driver.maximize_window()


source= driver.find_element(By.CSS_SELECTOR, "#angular")
target = driver.find_element(By.CSS_SELECTOR, "#droparea")

act_chains = ActionChains(driver)
#act_chains.drag_and_drop(source,target).perform()


act_chains\
     .click_and_hold(source)\
     .move_to_element(target)\
     .release()\
     .perform()


time.sleep(3)
driver.quit()
