from selenium.webdriver.common.by import By
from base_screen import BaseScreen


class HomeScreen(BaseScreen):
    screen_title = (By.XPATH, "//div/h1")
    start_for_free_btn = (By.XPATH, "//p/following-sibling::div/a[text()='Start for free']")
    email_field = (By.XPATH, "//*[@id='app']/div/div[1]/section[2]/form/div[1]/div/input")
    password_field = (By.XPATH, "//*[@id='app']/div/div[1]/section[2]/form/div[2]/div[1]/input")
    confirm_password_field = (By.XPATH, "//*[@id='app']/div/div[1]/section[2]/form/div[3]/div/input")
    submit_button = (By.XPATH, "//*[text()='Create your Qase account >']")
    agree_mark_box = (By.XPATH, "//label/input[@type='checkbox']/following-sibling::span")
    congratulation_label = (By.XPATH, "//div/h1")
    email_container = (By.XPATH, "//div/span")

    def __init__(self, driver):
        super().__init__(driver)

    def home_title(self):
        self.is_element_visible(self.screen_title)

    def is_congratulation_exist(self):
        self.is_element_visible(self.congratulation_label)

    def is_email_exist(self, email):
        assert email in self.get_element_text(self.email_container), "Email does not appear"

    def click_start_for_free_btn(self):
        self.click(self.start_for_free_btn)

    def click_agree_mark_box(self):
        self.click(self.agree_mark_box)

    def click_create_account_btn(self):
        self.click(self.submit_button)

    def enter_password(self, password):
        self.enter_data(self.password_field, password)

    def confirm_password(self, confirm_password):
        self.enter_data(self.confirm_password_field, confirm_password)

    def enter_email(self, email):
        self.enter_data(self.email_field, email)
