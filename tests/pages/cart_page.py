import logging

from selenium.webdriver.common.by import By
from tests.pages.base_page import BasePage

logger = logging.getLogger(__name__)

class CartPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    def remove_item(self):
        logger.debug("Finds the first “Remove” button on the cart page and clicks it.")
        remove_buttons = self.driver.find_elements(By.CSS_SELECTOR, ".cart_item .cart_button")
        if remove_buttons:
            remove_buttons[0].click()
