from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.core import driver

from pages.base_page import BasePage


class InventoryPage(BasePage):

    ADDTOCART_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")
    SHOPPINGCART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    PRODUCT_SORT_ELEMENT = (By.CLASS_NAME, "product_sort_container")
    sort_dropdown = ('class name', 'product_sort_container')

    def __init__(self, driver):
        super().__init__(driver)


    def click_add_backpack_to_cart(self):
        self.click(self.ADDTOCART_BUTTON)

    def click_shopping_cart_link(self):
        self.click(self.SHOPPINGCART_LINK)

    def select_product_sort(self, driver, text):
        dropdown_element = driver.find_element(*self.sort_dropdown)
        Select(dropdown_element).select_by_visible_text(text)
