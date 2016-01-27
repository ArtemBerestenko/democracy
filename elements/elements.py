__author__ = 'aberes'

from selenium.webdriver.support.ui import Select


class Selector():
    def __init__(self, locator):
        selector = Select(self.find_element(self.Organization_Type_locator))
        selector.select_by_index(org_type_index)
