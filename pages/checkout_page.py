from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class CheckoutPage(BasePage):

    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    CONFIRMATION_MESSAGE = (By.XPATH, "//*[@id=\"checkout_complete_container\"]/h2")


    def __init__(self, driver):
        super().__init__(driver)

    def enter_firstname(self, firstname):
        self.enter_text(self.FIRST_NAME, firstname)

    def enter_lastname(self, lastname):
        self.enter_text(self.LAST_NAME, lastname)

    def enter_postalcode(self, postalcode):
        self.enter_text(self.POSTAL_CODE, postalcode)

    def click_continue(self):
        self.click(self.CONTINUE_BUTTON)

    def continue_checkout(self, firstname, lastname, postalcode):
        self.enter_firstname(self.FIRST_NAME)
        self.enter_lastname(self.LAST_NAME)
        self.enter_postalcode(self.POSTAL_CODE)
        self.click_continue()

    def click_finish(self):
        self.click(self.FINISH_BUTTON)

    def get_confirmation_message(self):
        return self.get_text(self.CONFIRMATION_MESSAGE)