import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(7)
driver.get("http://londonfreelance.org/courses/frames/index.html")


frame_ele = driver.find_element(By.NAME, "main")
driver.switch_to.frame(frame_ele)

header_value = driver.find_element(By.XPATH, "//body/h2").text
print(header_value)

driver.switch_to.default_content()
driver.switch_to.parent_frame()



time.sleep(3)
driver.quit()
