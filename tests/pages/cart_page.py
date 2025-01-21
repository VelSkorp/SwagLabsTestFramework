import logging

from typing import List
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from tests.pages.base_logged_in_page import BaseLoggedInPage

logger = logging.getLogger(__name__)


class CartPage(BaseLoggedInPage):
    def __init__(self, driver):
        super().__init__(driver)

    def remove_item(self):
        logger.debug("Finds the first “Remove” button on the cart page and clicks it.")
        remove_buttons = self.driver.find_elements(
            By.CSS_SELECTOR, ".cart_item .cart_button"
        )
        if remove_buttons:
            remove_buttons[0].click()

    def get_items(self) -> List[WebElement]:
        logger.debug("Get cart items.")
        return self.driver.find_elements(By.CLASS_NAME, "cart_item")
