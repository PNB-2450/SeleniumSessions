import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


# @pytest.fixture(params=["chrome", "firefox", "Edge"], scope="class")
# def init_driver(request):
#     if request.param == "chrome":
#         web_driver = webdriver.Chrome(ChromeDriverManager().install())
#     if request.param == "firefox":
#         web_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
#     if request.param =="Edge":
#         web_driver = webdriver.Edge(EdgeChromiumDriverManager().install())
#     request.cls.driver = web_driver
#     yield
#     web_driver.close()


@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass


class Test_Google(BaseTest):
    def test_title(self):
        self.driver.get("https://google.com")
        assert self.driver.title == "Google"