from screens.home_screen import HomeScreen


class LoginNavigation(HomeScreen):

    def navigate_sign_up_page(self):
        print("login navigate func")
        assert self.home_title()
        self.start_for_free_btn()
        print("sign up navigation")

