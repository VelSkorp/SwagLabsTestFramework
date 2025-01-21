import logging

from selenium.webdriver.common.by import By

logger = logging.getLogger(__name__)


class LoginPage:
    URL = "https://www.saucedemo.com/"

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        logger.debug(f"Opens {self.URL} url.")
        self.driver.get(self.URL)

    def login(self, username, password):
        logger.debug(f"Logs in with {username} and {password}")
        username_input = self.driver.find_element(By.ID, "user-name")
        password_input = self.driver.find_element(By.ID, "password")
        login_button = self.driver.find_element(By.ID, "login-button")
        username_input.send_keys(username)
        password_input.send_keys(password)
        login_button.click()
