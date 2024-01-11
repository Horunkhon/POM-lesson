from tests.test_base import BaseTest
from actions.login_action import LoginAction


class TestSignUp(BaseTest):

    def test_signup(self):
        self.signup = LoginAction(self)
        assert self.signup.login_actions("exapmle@gmail.com", "123qweASD")
