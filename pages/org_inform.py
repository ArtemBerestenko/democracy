__author__ = 'aberes'

from base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from sign_in_new_org import SignInNewOrg


class OrgInformation(BasePage):
    title = "Sign Up - Organization Information - Democracy.com - Democracy.com"
    url = None

    def __init__(self, driv):
        super(OrgInformation, self).__init__(driv)

    # elment locators
    Your_Url_locator = (By.ID, "Url")
    Name_locator = (By.ID, "Name")
    Zip_Code_locator = (By.ID, "Zip")
    Phone_locator = (By.ID, "Phone")
    Party_locator = (By.ID, "PartyID")
    Short_Description_locator = (By.ID, "Tagline")
    Level_locator = (By.ID, "GeographicScope")
    SignUpButton_locator = (By.ID, "signUpComplete")

    def sign_up_button_click(self):
        """
        Click on Sign Up button
        :return: SignInNewOrg page
        """
        self.find_element(self.SignUpButton_locator).click()
        return SignInNewOrg(self.driver)

    def set_data(self, data):
        """
        Set data to page
        :param data: OrgInformationData class
        """
        self.set_text(self.Your_Url_locator, data.Your_Url)
        self.set_text(self.Name_locator, data.Name)
        self.set_text(self.Zip_Code_locator, data.Zip_Code)
        self.set_text(self.Phone_locator, data.Phone)
        self.set_text(self.Short_Description_locator, data.Short_Description)
        selector = Select(self.find_element(self.Party_locator))
        if type(data.Party) == int:
            selector.select_by_index(data.Party)
        else:
            selector.select_by_visible_text(data.Party)
        selector = Select(self.find_element(self.Level_locator))
        if type(data.Level) == int:
            selector.select_by_index(data.Level)
        else:
            selector.select_by_visible_text(data.Level)
