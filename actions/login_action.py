from navigations.signup_navigation import LoginNavigation
import time


class LoginAction(LoginNavigation):

    def login_actions(self, email, password):
        self.navigate_sign_up_page()
        print("navigation accept sign up")
        self.enter_email(email)
        self.enter_password(password)
        self.confirm_password(password)
        # self.agree_mark_box()
        self.click_create_account_btn()
        assert self.is_congratulation_exist(), "Sign up"
        self.is_email_exist(email)
        return True
