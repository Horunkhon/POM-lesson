from selenium import webdriver
import pytest


@pytest.fixture(params=["chrome", "mozilla"], scope="class")
def invoke_driver(request):
    global web_driver
    if request.par == "chrome":
        web_driver = webdriver.Chrome()
    web_driver.maximize_window()
    web_driver.get("https://qase.io/")
    request.cls.driver = web_driver
    web_driver.implicitly_wait(10)
    yield
    web_driver.close()
