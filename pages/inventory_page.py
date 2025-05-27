# pages/inventory_page.py
from selenium.webdriver.common.by import By
from .base_page import BasePage

class InventoryPage(BasePage):
    """Page object for the inventory (products) page."""
    # Locator for all product items on the page
    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")
    # Locator for the shopping cart link/icon
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def add_item_to_cart(self, item_name):
        """
        Add a product to the cart by its name.
        
        :param item_name: The exact name of the product to add.
        """
        items = self.driver.find_elements(*self.INVENTORY_ITEMS)
        for item in items:
            title = item.find_element(By.CLASS_NAME, "inventory_item_name").text
            if title == item_name:
                # Click the 'Add to cart' button
                add_button = item.find_element(By.CSS_SELECTOR, "button.btn_primary")
                add_button.click()
                break

    def go_to_cart(self):
        """Click on the shopping cart to navigate to the cart page."""
        self.click(*self.CART_LINK)
