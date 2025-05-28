# tests/test_login.py
import os
import pytest
from pages.login_page import LoginPage

@pytest.mark.usefixtures("driver")
class TestLogin:
    def test_valid_login(self, driver):
        """Test logging in with valid credentials redirects to inventory page."""
        login_page = LoginPage(driver)
        login_page.open()
        # Use environment variables, with defaults if not set
        username = os.getenv("SAUCE_USERNAME", "standard_user")
        password = os.getenv("SAUCE_PASSWORD", "secret_sauce")
        login_page.login(username, password)
        # Assert we are on the inventory page by checking the URL
        assert "inventory.html" in driver.current_url

    def test_invalid_login(self, driver):
        """Test logging in with invalid credentials shows an error message."""
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("invalid_user", "wrong_password")
        # The error message should contain the known "Epic sadface" text
        error_text = login_page.get_error_message()
        assert "Epic sadface" in error_text
