import time


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.driver import ChromeDriver

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("http://automationpractice.com/index.php")
driver.maximize_window()
driver.delete_all_cookies()

# click on sign in btn
driver.find_element(By.XPATH, "//a[@title='Log in to your customer account']").click()
time.sleep(5)
driver.find_element(By.ID, "email_create").send_keys('chanticrazy1@gmail.com')
login = driver.find_element(By.XPATH,"//i[@class='icon-user left']")
login.click()


driver.find_element(By.ID,"id_gender1").click()
driver.find_element(By.ID,"customer_firstname").send_keys("Chanti")
driver.find_element(By.ID, "customer_lastname").send_keys("Crazy")
driver.find_element(By.ID,"passwd").send_keys("Test@12345")

day_dd =driver.find_element(By.ID,'days')
day_dd.click()

def select_values(element, value):
    select = Select(element)
    select.select_by_value(value)

select_values(day_dd, '12')

month_dd=driver.find_element(By.ID,"months")
month_dd.click()
select_values(month_dd, '6')

year_dd = driver.find_element(By.ID,"years")
year_dd.click()
select_values(year_dd, "1993")

driver.find_element(By.ID,'address1').send_keys('2-87, Alabama')
driver.find_element(By.ID,"city").send_keys("Alabama")













driver.quit()