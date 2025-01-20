import pytest
import logging

from tests.pages.login_page import LoginPage
from tests.pages.products_page import ProductsPage
from tests.pages.cart_page import CartPage
from tests.pages.base_page import BasePage

logger = logging.getLogger(__name__)

@pytest.mark.usefixtures("driver")
def test_swag_labs_flow(driver):
    logger.info("Log in")
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    logger.info("Log (print) the products on the Products page")
    products_page = ProductsPage(driver)
    product_names = products_page.get_product_titles()
    logger.info("List of products on the page: %s", product_names)

    logger.info("Add the first item to your cart")
    products_page.add_first_item_to_cart()

    logger.info("Go to cart")
    base_page = BasePage(driver)
    base_page.go_to_cart()

    logger.info("Remove an item from the cart")
    cart_page = CartPage(driver)
    cart_page.remove_item()

    logger.info("Log out")
    base_page.open_menu_and_logout()
