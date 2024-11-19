import sys
import os
import logging
import pytest
import time
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from utils.config import BASE_URL, USERNAME, PASSWORD

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

def wait_for_element(self, locator, timeout=20):
    try:
        logging.info(f"Waiting for element: {locator} to be visible, timeout: {timeout} seconds")
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
    except TimeoutException:
        logging.error(f"Element {locator} not found after {timeout} seconds of waiting")
        raise

@pytest.fixture
def driver():
    # Setup WebDriver for GUI testing
    logging.info("Initializing Chrome WebDriver")
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    logging.info("Test completed, quitting WebDriver")
    driver.quit()

def test_valid_login(driver):
    logging.info("Starting test: Valid login")
    login_page = LoginPage(driver)
    login_page.navigate_to(BASE_URL)
    login_page.login(USERNAME, PASSWORD)
    logging.info("Test: Valid login completed")

def test_invalid_login(driver):
    logging.info("Starting test: Invalid login (incorrect username/password)")
    login_page = LoginPage(driver)
    login_page.navigate_to(BASE_URL)
    login_page.login("incorrect_username", "incorrect_password")
    logging.info("Test: Invalid login completed, the login should fail with incorrect credentials")
    time.sleep(5)
    assert login_page.is_error_message_displayed(), "Error message 'Invalid credentials' was not displayed."
