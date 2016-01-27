__author__ = 'aberes'

from selenium.webdriver.support.ui import WebDriverWait


class BasePage(object):
    def __init__(self, ver):
        self.driver = ver

    def get_title(self):
        """
        :return: title of the opened page
        """
        return self.driver.title

    def open(self):
        """
        open page using its URL and wait for page to be loaded
        :return: self
        """
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.wait_for_page_to_load(10)
        return self

    def is_opened(self):
        """
        Checks if page is opened
        :return: boolean
        """
        if self.get_title() == self.title:
            return True
        else:
            return False

    def find_element(self, locator):
        """
        finds element on page using its locator
        :param locator: element locator
        :return: element
        """
        return self.driver.find_element(*locator)

    def set_text(self, locator, text):
        """ Clear the input element at the specified locator and set specified text into it """
        self.find_element(locator).clear()
        if text != None:
            self.find_element(locator).send_keys(text)
        return self

    def close(self):
        """
        close page
        """
        self.driver.quit()

    def wait_for_page_to_load(self, time):
        """
        Waits for page to be loaded for established time
        :param time: time
        """
        WebDriverWait(self.driver, time).until(lambda s: self.title == self.driver.title, "Page did not load!!!")
