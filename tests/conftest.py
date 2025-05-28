# tests/conftest.py
import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="session")
def driver():
    """
    Pytest fixture to initialize a single WebDriver instance for all tests.
    This uses Chrome and can run in headless mode if HEADLESS=true.
    """
    options = Options()
    # Enable headless mode if requested (e.g., for CI environments)
    if os.getenv("HEADLESS", "true").lower() in ["true", "1", "yes"]:
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
    # Add arguments for compatibility in Linux containers
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Set up the Chrome WebDriver using webdriver-manager
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    yield driver
    driver.quit()
