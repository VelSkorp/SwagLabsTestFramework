import pytest
import logging

from tests.pages.login_page import LoginPage
from tests.pages.products_page import ProductsPage
from tests.pages.cart_page import CartPage

logger = logging.getLogger(__name__)


@pytest.mark.usefixtures("driver")
def test_swag_labs_flow(driver):
    logger.info("Log in")
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    assert (
        "inventory" in driver.current_url
    ), "After login we expect to get to /inventory.html"

    logger.info("Log (print) the products on the Products page")
    products_page = ProductsPage(driver)
    product_names = products_page.get_product_titles()
    logger.info("List of products on the page: %s", product_names)
    assert len(product_names) > 0, "Expect at least one item on the page"

    logger.info("Add the first item to your cart")
    products_page.add_first_item_to_cart()
    cart_count = products_page.get_cart_badge_count()
    assert cart_count == 1, f"After adding 1 item, the cart expects 1, not {cart_count}"

    logger.info("Go to cart")
    products_page.go_to_cart()
    assert (
        "cart" in driver.current_url
    ), f"Expected to get to /cart.html, not {driver.current_url}"

    cart_page = CartPage(driver)
    items_in_cart = cart_page.get_items()
    assert (
        len(items_in_cart) == 1
    ), f"Expected 1 item in the cart, but it turned out to be {len(items_in_cart)}"

    logger.info("Remove an item from the cart")
    cart_page.remove_item()
    items_in_cart_after_removal = cart_page.get_items()
    assert (
        len(items_in_cart_after_removal) == 0
    ), "Expect the cart to be empty after the item is deleted"

    logger.info("Log out")
    cart_page.open_menu_and_logout()
    assert (
        "saucedemo.com" in driver.current_url
    ), "The URL does not contain saucedemo.com, it seems we are not on the login page."


@pytest.mark.parametrize(
    "username,password,expected_url_part",
    [
        ("standard_user", "secret_sauce", "inventory"),
        ("invalid_user", "wrong_pass", "saucedemo.com"),
    ],
)
def test_login_flow(driver, username, password, expected_url_part):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(username, password)

    current_url = driver.current_url
    assert (
        expected_url_part in current_url
    ), f"Expected to have '{expected_url_part}' in the URL, but now: {current_url}"
