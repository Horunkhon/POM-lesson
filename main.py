from selenium import webdriver
from selenium.webdriver.common.by import By
import time
#
#
driver = webdriver.Chrome()
driver.maximize_window()
#
driver.get("http://qase.io")
time.sleep(5)
#
# driver.quit()


def testSignUp():
    email = "test@example.com"
    elemetn = driver.find_element(By.XPATH, "//div/h1")
    assert "All-in-one QA platform" in elemetn.text, "Page did not open"
    driver.find_element(By.XPATH, "//p/following-sibling::div/a[text()='Start for free']").click()
    time.sleep(5)
    driver.find_element(By.XPATH, "//*[@id='app']/div/div[1]/section[2]/form/div[1]/div/input").send_keys(email)
    driver.find_element(By.XPATH, "//*[@id='app']/div/div[1]/section[2]/form/div[2]/div[1]/input").send_keys("1234qwerty")
    driver.find_element(By.XPATH, "//*[@id='app']/div/div[1]/section[2]/form/div[3]/div/input").send_keys("1234qwerty")
    # driver.find_element(By.XPATH, "//label/input[@type='checkbox']/following-sibling::span").click()
    time.sleep(5)
    driver.find_element(By.XPATH, "//*[text()='Create your Qase account >']").click()
    congratulation_label = driver.find_element(By.XPATH, "//div/h1")
    email_container = driver.find_element(By.XPATH, "//div/span")
    assert "Congratulation!" in congratulation_label.text, "Sign up failed"
    assert email in email_container.text, "Email does not appear!!!"
    driver.close()

testSignUp()
