from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class CartPage(BasePage):

    CART_CONTAINER = (By.CLASS_NAME, "cart_contents_container")
    CART_ITEM = (By.CLASS_NAME,"cart_item")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    REMOVE_BUTTON = (By.ID, "remove-sauce-labs-backpack")


    def __init__(self, driver):
        super().__init__(driver)

    def is_item_displayed(self, CART_CONTAINER):
      return len(CART_CONTAINER) > 0

    def click_checkout(self):
        self.click(self.CHECKOUT_BUTTON)

    def remove_item(self,driver):
        REMOVE_BUTTON = (By.ID, "remove-sauce-labs-backpack")

        WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(REMOVE_BUTTON)
        )
        self.click(self.REMOVE_BUTTON)

    def is_cart_empty(self, driver):

        WebDriverWait(driver, 5).until(
            EC.url_contains("cart.html")
        )

        cart_container = driver.find_element(By.CLASS_NAME, "cart_contents_container")
        cart_list = cart_container.find_element(By.CLASS_NAME, "cart_list")
        cart_item = cart_list.find_elements(By.CSS_SELECTOR, ".cart_item")
        print(cart_item)
        print("outside",len(cart_item))
        if cart_item == []:

            return cart_item








