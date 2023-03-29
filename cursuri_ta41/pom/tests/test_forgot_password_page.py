import unittest
from pom.pages.forgot_password_page import ForgotPasswordPage
from pom.pages.login_page import LoginPage
from pom.tests.base_test import BaseTest


class TestForgotPasswordPage(BaseTest):
    INVALID_EMAIL = "asdf"
    INVALID_EMAIL_ERROR_MESSAGE = "Wrong email"
    ENTER_EMAIL_ERROR_MESSAGE = "Enter your email"

    def setUp(self) -> None:
        self.open_browser()

        self.login_page = LoginPage(self.driver)
        self.forgot_password_page = ForgotPasswordPage(self.driver)
        self.login_page.navigate_to_login_page()
        self.login_page.click_forgot_password_link()

    def tearDown(self) -> None:
        self.close_browser()

    def test_recover_password_with_invalid_email(self):
        self.forgot_password_page.set_email(self.INVALID_EMAIL)
        self.forgot_password_page.click_recover_button()
        self.assertTrue(self.forgot_password_page.is_email_error_message_displayed(), "Error message not displayed")
        self.assertEqual(self.forgot_password_page.get_email_error_message_text(), self.INVALID_EMAIL_ERROR_MESSAGE,
                         "Error message not displayed")

    def test_recover_password_with_empty_email(self):
        self.forgot_password_page.click_recover_button()
        self.assertTrue(self.forgot_password_page.is_email_error_message_displayed(), "Error message not displayed")
        self.assertEqual(self.forgot_password_page.get_email_error_message_text(), self.ENTER_EMAIL_ERROR_MESSAGE,
                         "Error message not displayed")