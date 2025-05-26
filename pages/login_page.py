# pages/login_page.py
from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):
    """Page object for the login page of Sauce Demo."""
    URL = "https://www.saucedemo.com"
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")

    def open(self):
        """Open the login page URL."""
        self.driver.get(self.URL)

    def login(self, username, password):
        """Enter credentials and submit the login form."""
        self.type(username, *self.USERNAME_INPUT)
        self.type(password, *self.PASSWORD_INPUT)
        self.click(*self.LOGIN_BUTTON)

    def get_error_message(self):
        """Return the text of any error message displayed."""
        return self.find(*self.ERROR_MESSAGE).text
