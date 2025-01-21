import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

logger = logging.getLogger(__name__)


class BaseLoggedInPage:
    def __init__(self, driver):
        self.driver = driver

    def open_menu_and_logout(self):
        logger.debug("Opens the burger menu and clicks Logout.")
        menu_button = self.driver.find_element(By.ID, "react-burger-menu-btn")
        menu_button.click()

        wait = WebDriverWait(self.driver, 10)
        logout_link = wait.until(
            expected_conditions.element_to_be_clickable((By.ID, "logout_sidebar_link"))
        )
        logout_link.click()

    def go_to_cart(self):
        logger.debug("Clicks shopping cart icon.")
        cart_button = self.driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        cart_button.click()

    def get_cart_badge_count(self) -> int:
        logger.debug("Get cart badge count.")
        cart_badge = self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
        return int(cart_badge.text)
