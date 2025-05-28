# tests/test_add_to_cart.py
import os
import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

def test_add_item_to_cart(driver):
    """
    Test that a user can log in, add an item to the cart, 
    and see the item listed in the shopping cart.
    """
    # Step 1: Log in with valid credentials
    login_page = LoginPage(driver)
    login_page.open()
    username = os.getenv("SAUCE_USERNAME", "standard_user")
    password = os.getenv("SAUCE_PASSWORD", "secret_sauce")
    login_page.login(username, password)

    # Step 2: Add a specific item to the cart
    inventory_page = InventoryPage(driver)
    item_name = "Sauce Labs Backpack"
    inventory_page.add_item_to_cart(item_name)
    # Navigate to the cart page
    inventory_page.go_to_cart()

    # Step 3: Verify the item is in the cart
    cart_page = CartPage(driver)
    items = cart_page.get_cart_items()
    assert item_name in items
