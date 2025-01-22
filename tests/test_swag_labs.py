import pytest
import logging

from tests.pages.login_page import LoginPage
from tests.pages.products_page import ProductsPage
from tests.pages.cart_page import CartPage

logger = logging.getLogger(__name__)


@pytest.mark.usefixtures("driver")
def test_list_products(logged_in):
    logger.info("Log (print) the products on the Products page")
    products_page = ProductsPage(logged_in)
    product_names = products_page.get_product_titles()
    logger.info("List of products on the page: %s", product_names)
    assert len(product_names) > 0, "Expect at least one item on the page"


@pytest.mark.usefixtures("driver")
def test_add_first_item_to_cart(logged_in):
    logger.info("Add the first item to your cart")
    products_page = ProductsPage(logged_in)
    products_page.add_first_item_to_cart()
    cart_count = products_page.get_cart_badge_count()
    assert cart_count == 1, f"After adding 1 item, the cart expects 1, not {cart_count}"


@pytest.mark.usefixtures("driver")
def test_go_to_cart_page(logged_in):
    logger.info("Go to cart")
    products_page = ProductsPage(logged_in)
    products_page.add_first_item_to_cart()
    products_page.go_to_cart()
    assert (
        "cart" in logged_in.current_url
    ), f"Expected to get to /cart.html, not {logged_in.current_url}"


@pytest.mark.usefixtures("driver")
def test_cart_has_single_item(logged_in):
    logger.info("Add an item to the cart and verify it contains exactly 1 item")
    products_page = ProductsPage(logged_in)
    products_page.add_first_item_to_cart()
    products_page.go_to_cart()

    cart_page = CartPage(logged_in)
    items_in_cart = cart_page.get_items()
    assert (
        len(items_in_cart) == 1
    ), f"Expected 1 item in the cart, but it turned out to be {len(items_in_cart)}"


@pytest.mark.usefixtures("driver")
def test_remove_item_from_cart(logged_in):
    products_page = ProductsPage(logged_in)
    products_page.add_first_item_to_cart()
    products_page.go_to_cart()

    logger.info("Remove an item from the cart")
    cart_page = CartPage(logged_in)
    cart_page.remove_item()
    items_in_cart_after_removal = cart_page.get_items()
    assert (
        len(items_in_cart_after_removal) == 0
    ), "Expect the cart to be empty after the item is deleted"


@pytest.mark.parametrize(
    "username,password,expected_url_part",
    [
        ("standard_user", "secret_sauce", "inventory"),
        ("invalid_user", "wrong_pass", "saucedemo.com"),
    ],
)
def test_login_form(driver, username, password, expected_url_part):
    logger.info(
        f"Attempting to log in with username='{username}', password='{password}'"
    )
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(username, password)

    current_url = driver.current_url
    assert (
        expected_url_part in current_url
    ), f"Expected to have '{expected_url_part}' in the URL, but now: {current_url}"
