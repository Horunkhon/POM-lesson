from selenium import webdriver
import pytest


@pytest.fixture(params=["chrome", "mozilla"], scope="class")
def invoke_driver(request):
    global driver
    if request.param == "chrome":
        driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://qase.io/")
    request.cls.driver = driver
    driver.implicitly_wait(10)
    yield
    driver.close()
