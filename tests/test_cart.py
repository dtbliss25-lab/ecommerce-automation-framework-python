from selenium.webdriver.common.by import By

from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


def test_empty_cart(users_data, driver):

    CART_ITEM = (By.CLASS_NAME, "cart_contents_container")
    login_page = LoginPage(driver)

    driver.get("https://www.saucedemo.com")

    user = users_data["valid_user"]

    login_page.login(
        user["username"],
        user["password"]
    )

    inventory_page = InventoryPage(driver)

    inventory_page.click_shopping_cart_link()

    cart_page = CartPage(driver)

    assert cart_page.is_item_displayed(CART_ITEM) is True, "Cart should be empty"