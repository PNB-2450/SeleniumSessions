from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

opetions = webdriver.ChromeOptions()
opetions.add_argument('--headless')

driver = webdriver.Chrome(ChromeDriverManager().install(),options=opetions)
driver.implicitly_wait(5)
driver.get('https://pythonbasics.org/selenium-screenshot/')

#driver.get_screenshot_as_file('screenshot1.png')


# Make sure that you are running on headless mode for whole page screenshot

S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
driver.set_window_size(S('Width'),S('Height'))
driver.find_element(By.TAG_NAME,'body').screenshot('get_screenshot1.png')


driver.quit()




driver.quit()