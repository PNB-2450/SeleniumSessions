from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from webdriver_manager.chrome import ChromeDriverManager
import time
d=webdriver.Chrome(ChromeDriverManager().install())
d.implicitly_wait(10)
d.get("https://sm.clarksfield.com/")
d.maximize_window()


email = "nagendra@scaledesk.xyz"
password = "Test@12345"

#Click on Login
d.find_element_by_xpath("//span[@data-event_name='menu-login']").click()

email_ele = d.find_element_by_id('input__email')
time.sleep(3)
password_ele = d.find_element_by_id("input_password")
login_ele = d.find_element_by_xpath("//span[@data-event_name='loginnow']")

#Enter Email & Password Using ActionChains Class
action = ActionChains(d)
action.send_keys_to_element(email_ele, email)
action.send_keys_to_element(password_ele, password)
action.click(login_ele).perform()


print(d.title)
if Alert is True:
    alert = Alert(d).text
    print(alert)
else:
    print('There is no alert')
