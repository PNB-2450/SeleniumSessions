from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


#   Headless Chrome Browser
# options = webdriver.ChromeOptions()
# options.headless=True
# d=webdriver.Chrome(ChromeDriverManager().install(),options=options)

# # Headless Firefox browser
# options = webdriver.FirefoxOptions()
# options.headless=True
# d=webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)


# Incognito browser
options = webdriver.ChromeOptions()
#options.headless=False
options.add_argument('--headless')
d=webdriver.Chrome(ChromeDriverManager().install(), options= options)


d.implicitly_wait(10)
d.get("https://sm.clarksfield.com/")
d.maximize_window()
print(d.title)

if Alert is True:
     alert = Alert(d).text
     print("message is: ", alert)
else:
    print("There is no alert found")
d.quit()


