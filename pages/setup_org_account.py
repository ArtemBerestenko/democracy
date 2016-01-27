__author__ = 'aberes'

from pages.base_page import BasePage
from pages.org_inform import OrgInformation
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class SetupOrgAccount(BasePage):
    title = "Sign Up - Account Info - Democracy.com - Democracy.com"
    url = "http://staging.democracy.com/signup/SetupOrgAccount"

    def __init__(self, driv):
        super(SetupOrgAccount, self).__init__(driv)

    # elments
    Your_Email_locator = (By.ID, "Email")
    Confirm_Email_locator = (By.ID, "ConfirmEmail")
    Password_locator = (By.ID, "Password")
    Organization_Type_locator = (By.ID, "OrgType")
    Next_Step_Button_locator = (By.XPATH, "//button[contains(., 'Next Step')]")

    # methods:
    def login(self, email, conf_email, password, org_type_value):
        """
        Sets data to page elements
        :param email:
        :param conf_email:
        :param password:
        :param org_type_value:
        """
        selector = Select(self.find_element(self.Organization_Type_locator))

        if type(org_type_value) == int:
            selector.select_by_index(org_type_value)
        else:
            selector.select_by_visible_text(org_type_value)
        self.set_text(self.Your_Email_locator, email)
        self.set_text(self.Confirm_Email_locator, conf_email)
        self.set_text(self.Password_locator, password)

    def next_step_click(self):
        """
        clicks on Hext Step button
        :return: OrgInformation page
        """
        self.find_element(self.Next_Step_Button_locator).click()
        return OrgInformation(self.driver)
