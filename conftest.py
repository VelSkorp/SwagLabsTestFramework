import pytest
import logging
from tests.browser_factory import BrowserFactory
from tests.pages.login_page import LoginPage
from tests.pages.base_logged_in_page import BaseLoggedInPage

logger = logging.getLogger(__name__)


def pytest_addoption(parser):
    """
    Add a custom --browser option to select a browser when running tests:
      pytest --browser firefox
    Default = chrome.
    """
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to run tests (chrome or firefox)",
    )


@pytest.fixture(scope="session", autouse=True)
def configure_logging():
    """
    A fixture for configuring session-level logging.
    """
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # Customizing the format
    formatter = logging.Formatter("[%(levelname)s] %(asctime)s - %(name)s: %(message)s")

    # Processing logs to the console
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # Remove possible rehandlers if the fixture is invoked more than once
    if not logger.handlers:
        logger.addHandler(console_handler)

    yield


@pytest.fixture(scope="function")
def driver(request):
    browser_name = request.config.getoption("--browser")
    driver = BrowserFactory.create_driver(browser_name)
    yield driver
    driver.quit()


@pytest.fixture
def logged_in(driver):
    logger.info("Log in")
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    assert (
        "inventory" in driver.current_url
    ), "After login we expect to get to /inventory.html"

    yield driver

    logger.info("Log out")
    base_logged_in = BaseLoggedInPage(driver)
    base_logged_in.open_menu_and_logout()
    assert (
        "saucedemo.com" in driver.current_url
    ), "The URL does not contain saucedemo.com, it seems we are not on the login page."
