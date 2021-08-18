import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(scope="class")
def init_chrome_driver(request):
    ch_driver=webdriver.Chrome(ChromeDriverManager().install())
    request.cls.driver = ch_driver

    yield
    ch_driver.close()


@pytest.fixture(scope="class")
def init_ff_driver(request):
    ff_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    request.cls.driver = ff_driver
    yield
    ff_driver.close()

@pytest.mark.usefixtures("init_chrome_driver")
class Base_Chrome_Test:
    pass

@pytest.mark.usefixtures("init_ff_driver")
class Base_FF_Test:
    pass

class Test_Google_Chrome(Base_Chrome_Test):
    def test_title(self):
        self.driver.get("https://www.google.com")
        assert self.driver.title =="Google"

    def test_url(self):
        url = self.driver.current_url
        assert url == "https://www.google.com/"

class Test_Gmail_FF(Base_FF_Test):
    def test_title(self):
        self.driver.get("https://www.gmail.com")
        title = self.driver.title
        assert title == "Gmail"

    def test_url(self):
        url = self.driver.current_url
        assert url == "https://www.gmail.com/"


