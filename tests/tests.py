__author__ = 'aberes'

import time

from selenium import webdriver
from proboscis.decorators import test
from setup_org_account import SetupOrgAccount
from proboscis.asserts import *
from dataclasses import *

driver = webdriver.Firefox()


@test
class RegistrationTest():
    @test
    def create_organization_1(self):
        sign_up_account_page = SetupOrgAccount(driver)
        sign_up_account_page.open()
        assert_true(sign_up_account_page.is_opened(), "Setup organization website Page did not opened")
        email = "female" + "%s" % time.strftime('%H/%M/%S/%d/%m/%Y') + "@gmail.com"
        sign_up_account_page.login(email, email, "softserve1", "Political action committee")
        org_info_sign_in_page = sign_up_account_page.next_step_click()
        assert_true(org_info_sign_in_page.is_opened(), "Organization Info Page did not open")
        org_data = OrgInformationData()
        org_data.Your_Url = "%s" % time.strftime('%H%M%S%d%m%Y')
        org_data.Name = "Big Organization"
        org_data.Zip_Code = "10160"
        org_data.Phone = "1234567890"
        org_data.Party = "American Party"
        org_data.Level = "Nationwide - display in any search"
        org_info_sign_in_page.set_data(org_data)
        welcome_page = org_info_sign_in_page.sign_up_button_click()
        assert_true(welcome_page.is_opened(), "Succesful registration page did not opened")

    @test
    def create_organization_2(self):
        sign_up_account_page = SetupOrgAccount(driver)
        sign_up_account_page.open()
        assert_true(sign_up_account_page.is_opened(), "Setup organization website Page did not opened")
        email = "bal" + "%s" % time.strftime('%H/%M/%S/%d/%m/%Y') + "@gmail.com"
        sign_up_account_page.login(email, email, "softserve1", "Ballot measure committee")
        org_info_sign_in_page = sign_up_account_page.next_step_click()
        assert_true(org_info_sign_in_page.is_opened(), "Organization Info Page did not open")
        org_data = OrgInformationData()
        org_data.Your_Url = "%s" % time.strftime('%H%M%S%d%m%Y')
        org_data.Name = "Small Organization"
        org_data.Zip_Code = "35004"
        org_data.Phone = "(123)456-7890"
        org_data.Party = "Democrat Nonpartisan League"
        org_data.Short_Description = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque ornare ultrices"
        org_data.Level = "Statewide - display in searches of your state"
        org_info_sign_in_page.set_data(org_data)
        welcome_page = org_info_sign_in_page.sign_up_button_click()
        assert_true(welcome_page.is_opened(), "Succesful registration page did not opened")

    @test
    def create_organization_3(self):
        sign_up_account_page = SetupOrgAccount(driver)
        sign_up_account_page.open()
        assert_true(sign_up_account_page.is_opened(), "Setup organization website Page did not opened")
        email = "soc" + "%s" % time.strftime('%H/%M/%S/%d/%m/%Y') + "@gmail.com"
        sign_up_account_page.login(email, email, "!2#4%6&8*9)", "501(c)(4) social welfare organization")
        org_info_sign_in_page = sign_up_account_page.next_step_click()
        assert_true(org_info_sign_in_page.is_opened(), "Organization Info Page did not open")
        org_data = OrgInformationData()
        org_data.Your_Url = "%s" % time.strftime('%H%M%S%d%m%Y')
        org_data.Name = "New"
        org_data.Zip_Code = "10001"
        org_data.Phone = "1234-567890"
        org_data.Party = "Constitutional"
        org_data.Short_Description = "Lorem ipsum dolor sit amet"
        org_data.Level = "Nationwide - display in any search"
        org_info_sign_in_page.set_data(org_data)
        welcome_page = org_info_sign_in_page.sign_up_button_click()
        assert_true(welcome_page.is_opened(), "Succesful registration page did not opened")
