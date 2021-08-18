from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from webdriver_manager.chrome import ChromeDriverManager

d=webdriver.Chrome(ChromeDriverManager().install())
d.implicitly_wait(10)
d.get("https://sm.clarksfield.com/")
d.maximize_window()

d.find_element_by_xpath("//span[@data-event_name='menu-login']").click()

email = "nagendra@scaledesk.xyz"
password = "Test@12345"

d.find_element_by_id('input__email').send_keys(email)
d.find_element_by_id("input_password").send_keys(password)
d.find_element_by_xpath("//span[@data-event_name='loginnow']").click()

print(d.title)

if Alert is True:
     alert = Alert(d).text
     print("message is: ", alert)
else:
    print("There is no alert found")
d.quit()


