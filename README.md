# SwagLabsTestFramework

A minimal test framework in Python that automates the https://www.saucedemo.com/ site using:
- Page Object pattern
- Browser Factory (supporting Chrome/Firefox)
- Logging (using Python’s `logging` module)
- `pytest` for test execution
- `webdriver_manager` for automatically managing browser drivers

## Requirements

- Python 3.8+
- pip (Python package manager)
- Chrome or Firefox installed (for headless testing, make sure you have the necessary browser versions).
- ChromeDriver or GeckoDriver – though `webdriver_manager` will install drivers automatically in most cases.
- (Optionally) a virtual environment tool like venv or conda.

## Installation and Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/VelSkorp/SwagLabsTestFramework.git
    cd SwagLabsTestFramework
    ```

2. Create and activate a virtual environment (recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Linux/Mac
    # On Windows: venv\Scripts\activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. (Optional) Verify installation:
    ```bash
    pytest --version
    python --version
    ```

## How to Run Tests

1. Default run (Chrome browser, headless mode):
    ```bash
    pytest
    ``` 
    By default, it will look for all test files matching test_*.py in the tests directory.

2. Run tests in Firefox:
    ```bash
    pytest --browser firefox
    ```

3. See detailed logs:
    - By default, the log level is set to `INFO` in `conftest.py`.
    - Logs are printed to the console.

4. Specific test file:
    ```bash
    pytest tests/test_swag_labs.py
    ```

## Test Scenarios

1. `test_list_products`
    - Logs in (using the `logged_in` fixture).
    - Retrieves and logs all products on the Products page.
    - Asserts there is at least one product listed.

2. `test_add_first_item_to_cart`
    - Logs in.
    - Adds the first item to the cart.
    - Checks that the cart badge shows exactly 1 item.

3. `test_go_to_cart_page`
    - Logs in.
    - Adds an item to the cart.
    - Navigates to the cart page.
    - Verifies that the current URL contains `/cart.html`.

4. `test_cart_has_single_item`
    - Logs in.
    - Adds one item to the cart and navigates there.
    - Verifies that the cart contains exactly 1 item.

5. `test_remove_item_from_cart`
    - Logs in.
    - Adds an item to the cart; navigates to the cart.
    - Removes the item.
    - Checks that the cart is empty afterward.

6. `test_login_form` (parametrized)
    - Runs with multiple sets of credentials:
        - **Valid**: `standard_user`, `secret_sauce`
            - Expects to see "`inventory`" in the URL.
        - **Invalid**: `invalid_user`, `wrong_pass`
            - Expects the URL to contain "`saucedemo.com`" but not "`inventory`".
    - Demonstrates how to handle multiple test inputs with `@pytest.mark.parametrize`.

## Additional Notes

- **Logging**:
    - Configured in `conftest.py` with a `pytest` fixture named `configure_logging`.
    - By default prints logs to the console with level `INFO`. You can adjust the level or add file handlers if needed.
- **Headless Browsers**:
    - Both Chrome and Firefox are configured in headless mode via `--headless=new`. Remove or change the arguments if you want to see the browser UI.
- **BaseLoggedInPage**:
    - A parent class for pages that assume the user is already logged in.
    - In its constructor (or methods), you can add checks to ensure the user is logged in (e.g., checking for specific elements).

## Contributing

Contributions are welcome! Please submit issues or pull requests with any improvements, bug fixes, or new features.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.