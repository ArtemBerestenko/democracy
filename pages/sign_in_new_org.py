__author__ = 'aberes'

from pages.base_page import BasePage


class SignInNewOrg(BasePage):
    title = "Welcome to Democracy.com - Democracy.com"
    url = "http://staging.democracy.com/signup/SignInNewOrg"

    def __init__(self, driv):
        super(SignInNewOrg, self).__init__(driv)
