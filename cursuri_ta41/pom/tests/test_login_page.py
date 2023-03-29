import unittest

from pom.pages.base_page import BasePage
from pom.pages.login_page import LoginPage
from pom.tests.base_test import BaseTest


class TestLoginPage(BaseTest):
    MAIN_ERROR_MESSAGE = "Login was unsuccessful. Please correct the errors and try again.\nNo customer account found"
    EMPTY_EMAIL_ERROR_MESSAGE = "Please enter your email"
    WRONG_EMAIL = "email.exemplu@yahoo.com"
    WRONG_PASS = "somepass"

    def setUp(self) -> None:
        self.open_browser()
        self.login_page = LoginPage(self.driver)

    def tearDown(self) -> None:
        self.close_browser()

    def test_login_with_unregistered_email(self):
        self.login_page.navigate_to_login_page()
        self.login_page.set_email(self.WRONG_EMAIL)
        self.login_page.set_password(self.WRONG_PASS)
        self.login_page.click_login_button()

        self.assertTrue(self.login_page.is_main_error_message_displayed(), "Main error message not displayed.")
        self.assertEqual(self.login_page.get_main_error_message_text(), self.MAIN_ERROR_MESSAGE, "Unexpected error " +
                         "message.")

    def test_login_with_empty_email_and_pass(self):
        self.login_page.navigate_to_login_page()
        self.login_page.click_login_button()

        self.assertTrue(self.login_page.is_email_error_message_displayed(), "Email error message not displayed.")
        self.assertEqual(self.login_page.get_email_error_message_text(), self.EMPTY_EMAIL_ERROR_MESSAGE, "Unexpected "
                                                                                                         "error "
                                                                                                         "message.")
