import unittest

from selenium import webdriver

from pom.utils.driverfactory import DriverFactory


class BaseTest(unittest.TestCase):
    driver: webdriver

    def open_browser(self):
        self.driver = DriverFactory.get_driver()

    def close_browser(self):
        self.driver.quit()