import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures('init_driver')
class BaseTest():
    pass


class Test_Firsttest(BaseTest):

    @pytest.mark.parametrize(
                             'username, password',
                               [
                                 ("test@gmail.com", "test@12345"),
                                 ("test2@gmail.com", "test@123456")
                               ]
                             )
    def test_method(self, username, password):
        self.driver.get("https://smartmoney.angelbroking.com/login/")
        #self.driver.switch_to.alert.dismiss()

        self.driver.find_element(By.ID, 'deny').click()
        self.driver.find_element(By.CLASS_NAME, 'wewidgeticon we_close').click()



        self.driver.find_element(By.ID, 'input__email')
        self.driver.find_element(By.ID, 'input_password')
