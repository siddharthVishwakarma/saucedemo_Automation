# pages/base_page.py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    """Base class for all page objects."""
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10

    def find(self, *locator):
        """Wait for an element to be visible and return it."""
        return WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def click(self, *locator):
        """Wait for an element to be clickable and click it."""
        element = WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    def type(self, text, *locator):
        """Wait for an input field, clear it, and type text."""
        element = self.find(*locator)
        element.clear()
        element.send_keys(text)

    def open(self, url):
        """Navigate to a URL."""
        self.driver.get(url)
