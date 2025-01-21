import pytest
import logging
from tests.browser_factory import BrowserFactory


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
