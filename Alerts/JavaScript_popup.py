from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("https://mail.rediff.com/cgi-bin/login.cgi")
driver.maximize_window()

driver.find_element(By.NAME, 'proceed').click()
time.sleep(3)

alert = driver.switch_to.alert
print(alert.text)
alert.accept()  # For accept the alert & click on OK
#alert.dismiss()   # For cancel the alert

# To enter the any text into java cript popups
#alert.send_keys("Thist is seleniumm")

# For came back from popup
driver.switch_to.default_content()
driver.switch_to.alert.dismiss()








time.sleep(3)
driver.quit()