from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    USERNAME_INPUT = (By.NAME, "username")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.CLASS_NAME, "orangehrm-login-button")
    ERROR_MESSAGE = (By.CLASS_NAME, "oxd-alert-content-text")

    def login(self, username, password):
        self.wait_for_element(self.USERNAME_INPUT).send_keys(username)
        self.wait_for_element(self.PASSWORD_INPUT).send_keys(password)
        self.wait_for_element(self.LOGIN_BUTTON).click()

    def is_error_message_displayed(self):
        error_message_element = self.wait_for_element(self.ERROR_MESSAGE)
        return "Invalid credentials" in error_message_element.text