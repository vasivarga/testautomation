import time
import unittest
from unittest import TestCase

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

"""
########### Libraria unittest ###########

Libraria unittest ofera suport pentru crearea de teste rulabile direct in interiorul clasei.
Se implementeaza prin mostenirea clasei TestCase din libraria unittest
Orice clasa de teste trebuie sa mosteneasca clasa TestCase si sa aiba urmatoarele particularitati:
1. metoda setUp() -> toate activitatile care trebuie sa fie executate inainte de ORICE TEST din clasa respectiva
2. metoda teardown() -> toate activitatile care trebuie sa fie executate dupa de ORICE TEST din clasa respectiva
3. toate metodele de test trebuie sa aiba prefixul test_
"""


class Test(TestCase):

    driver = None
    LINK = "https://formy-project.herokuapp.com/form"
    BUTTON_SUBMIT = (By.XPATH, "//a[text()='Submit']")
    MESSAGE_SUCCESS = (By.CLASS_NAME, "alert-success")

    # suprascriem metoda setUp care va rula inainte de fiecare test
    def setUp(self):
        print(f"Se executa ce este in setUp() pentru {self._testMethodName}")
        self.driver = webdriver.Chrome()
        self.driver.get(self.LINK)
        self.driver.maximize_window()
        time.sleep(1)

    # suprascriem metoda tearDown care va rula dupa fiecare test
    def tearDown(self):
        print(f"Se executa ce este in tearDown() pentru {self._testMethodName}\n")
        self.driver.quit()

    # metoda ajutatoare - ea nu va fi rulata ca test pentru ca nu are prefixul test_
    def wait_for_element_to_be_present(self, element_locator, seconds_to_wait):
        wait = WebDriverWait(self.driver, seconds_to_wait)
        return wait.until(EC.presence_of_element_located(element_locator))

    def test_url(self):
        print(f"A inceput testul {self._testMethodName}")

        expected_url = "https://formy-project.herokuapp.com/form"
        actual_url = self.driver.current_url

        assert expected_url == actual_url, f"Invalid URL, expected {expected_url}, but found {actual_url}"

    def test_title(self):
        print(f"A inceput testul {self._testMethodName}")

        expected_title = "Formy"
        actual_title = self.driver.title

        assert expected_title == actual_title, f"Invalid title, expected {expected_title}, but found {actual_title}"

    def test_form_submitted(self):
        print(f"A inceput testul {self._testMethodName}")

        submit_button = self.driver.find_element(*self.BUTTON_SUBMIT)
        submit_button.click()

        mesaj_succes = self.wait_for_element_to_be_present(self.MESSAGE_SUCCESS, 1)
        assert mesaj_succes.is_displayed(), f'Message not displayed!'

    # dam skip la test
    @unittest.skip
    def test_a_picat(self):
        print(f"A inceput testul {self._testMethodName}")
        assert False, "Test picat"
