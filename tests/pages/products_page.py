import logging

from selenium.webdriver.common.by import By
from tests.pages.base_logged_in_page import BaseLoggedInPage

logger = logging.getLogger(__name__)


class ProductsPage(BaseLoggedInPage):
    def __init__(self, driver):
        super().__init__(driver)

    def get_product_titles(self) -> list[str]:
        logger.debug("Returns a list of product names on the page.")
        product_elements = self.driver.find_elements(
            By.CLASS_NAME, "inventory_item_name"
        )
        return [element.text for element in product_elements]

    def add_first_item_to_cart(self):
        logger.debug("Finds the first “Add to cart” button on the page and clicks it.")
        add_buttons = self.driver.find_elements(
            By.CSS_SELECTOR, ".inventory_list .btn_inventory"
        )
        if add_buttons:
            add_buttons[0].click()
