from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from p6_pom_bdd.browser import Browser


class BasePage(Browser):
    SEARCH_INPUT = (By.ID, "small-searchterms")
    SEARCH_BUTTON = (By.XPATH, "//button[text()='Search']")

    BASE_URL = "https://demo.nopcommerce.com/"

    # Functie care asteapta pana cand un Web Element apare in pagina
    # Primeste 2 parametri:
    # element_locator - locatorul elementului dupa care va astepta (sub forma de tuplu)
    # seconds_to_wait - cantitatea maxima de asteptare in secunde
    def wait_for_element_to_be_present(self, element_locator, seconds_to_wait):
        wait = WebDriverWait(self.driver, seconds_to_wait)
        return wait.until(expected_conditions.presence_of_element_located(element_locator))

    # Functie care cauta si returneaza un Web Element dupa un locator dat
    def find(self, locator):
        return self.driver.find_element(*locator)

    # Functie care cauta si returneaza o lista cu Web Elements dupa un locator dat (sub forma de tuplu)
    # Daca nu gaseste nimic, va returna o lista goala
    def find_all(self, locator):
        return self.driver.find_elements(*locator)

    # Functie care da click pe un Web Element
    def click(self, locator):
        self.find(locator).click()

    # Functie care scrie pe un Web Element
    # Primeste 2 parametri:
    # locator - locatorul elementului pe care se va scrie (sub forma de tuplu)
    # text - textul care urmeaza a fi scris
    def type(self, locator, text):
        self.find(locator).send_keys(text)

    def is_element_displayed(self, locator):
        return self.find(locator).is_displayed()

    # Returneaza textul de pe un Web Element
    def get_element_text(self, locator):
        return self.find(locator).text

    def clear(self, locator):
        self.find(locator).clear()

    # va returna True daca expected_url este egal cu URL-ul
    # paginii din care apelam metoda
    def is_url_correct(self, expected_url):
        return expected_url == self.driver.current_url

    # deoarece textbox-ul de cautare e prezent in toate paginile, definim functia care scrie pe el in BasePage
    # astfel functia va putea fi apelata in orice pagina
    def type_text_on_search_input(self, text):
        self.type(self.SEARCH_INPUT, text)

    # deoarece butonul de cautare e prezent in toate paginile, definim functia care face clickpe el in BasePage
    # astfel functia va putea fi apelata in orice pagina
    def click_search_button(self):
        self.click(self.SEARCH_BUTTON)

    # Functie care selecteaza o optiune de pe un dropdown dupa textul dat.
    # Functia are 2 parametri:
    # dropdown_locator - locatorul dropdown-ului (sub forma de tuplu)
    # text_to_select - textul optiunii pe care vrem sa o selectam
    def select_dropdown_option_by_text(self, dropdown_locator, text_to_select):
        dropdown_element = self.find(dropdown_locator)
        select = Select(dropdown_element)
        select.select_by_visible_text(text_to_select)

    # Functie care selecteaza un checkbox
    def check_checkbox(self, checkbox_locator):
        checkbox_element = self.find(checkbox_locator)

        # daca checkbox-ul nu este selectat (bifat), va da click pe el
        if not checkbox_element.is_selected():
            checkbox_element.click()

    # Functie care deselecteaza un checkbox
    def uncheck_checkbox(self, checkbox_locator):
        checkbox_element = self.find(checkbox_locator)

        # daca checkbox-ul este selectat (bifat), va da click pe el
        if checkbox_element.is_selected():
            checkbox_element.click()
