from selenium.webdriver.common.by import By

from p6_pom_bdd.pages.base_page import BasePage


class SearchResultsPage(BasePage):
    PRODUCT_ITEM = (By.CLASS_NAME, "product-item")
    PRODUCT_TITLE = (By.CLASS_NAME, "product-title")

    # verifica daca avem produse afisate
    def are_all_products_displayed(self):
        self.wait_for_element_to_be_present(self.PRODUCT_ITEM, 3)
        product_item_list = self.find_all(self.PRODUCT_ITEM)

        # daca gaseste vreun produs ce nu este afisat, returneaza fals si iese imediat din functie
        for item in product_item_list:
            if not item.is_displayed():
                return False

        return True

    # verifica daca toate titlurile de produs un text dat
    def are_all_titles_containing_text(self, text: str):
        titles_list = self.find_all(self.PRODUCT_TITLE)

        # daca gaseste vreun titlu ce nu contine un text cautat, returneaza fals si iese imediat din functie
        for title in titles_list:
            if text.lower() not in title.text.lower():
                return False

        return True
