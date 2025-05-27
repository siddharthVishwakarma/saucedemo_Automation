# pages/cart_page.py
from selenium.webdriver.common.by import By
from .base_page import BasePage

class CartPage(BasePage):
    """Page object for the shopping cart page."""
    # Locator for the names of items in the cart
    ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")

    def get_cart_items(self):
        """
        Get a list of item names currently in the cart.
        
        :return: List of item name strings.
        """
        elements = self.driver.find_elements(*self.ITEM_NAMES)
        return [elem.text for elem in elements]
