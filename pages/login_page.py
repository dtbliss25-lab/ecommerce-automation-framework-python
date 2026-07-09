from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):

    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.XPATH, "//h3")

    def __init__(self, driver):
        super().__init__(driver)

    def enter_username(self, username):
        self.enter_text(self.USERNAME, username)

    def enter_password(self, password):
        self.enter_text(self.PASSWORD, password)

    def click_login(self):
        self.click(self.LOGIN_BUTTON)

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)