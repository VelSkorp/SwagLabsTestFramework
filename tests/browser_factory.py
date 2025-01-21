from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


class BrowserFactory:
    @staticmethod
    def create_driver(browser_name: str = "chrome"):
        browser_name = browser_name.lower()

        if browser_name == "chrome":
            chrome_options = ChromeOptions()
            chrome_options.add_argument("--headless=new")
            chrome_options.add_argument("--start-maximized")
            service = ChromeService(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=chrome_options)
            return driver

        elif browser_name == "firefox":
            firefox_options = FirefoxOptions()
            firefox_options.add_argument("--headless=new")
            firefox_options.add_argument("--start-maximized")
            service = FirefoxService(GeckoDriverManager().install())
            driver = webdriver.Firefox(service=service, options=firefox_options)
            return driver

        else:
            raise ValueError(f"Unknown browser: {browser_name}")
