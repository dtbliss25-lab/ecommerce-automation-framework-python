from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

def test_remove_product_from_cart(users_data, driver):

    CART_CONTAINER = (By.CLASS_NAME, "cart_contents_container")
    CART_ITEM = (By.CLASS_NAME,"cart_item")
    REMOVE_BUTTON = (By.ID, "remove-sauce-labs-backpack")

    login_page = LoginPage(driver)

    driver.get("https://www.saucedemo.com")

    user = users_data["valid_user"]

    login_page.login(
        user["username"],
        user["password"]
    )

    inventory_page = InventoryPage(driver)

    inventory_page.click_add_backpack_to_cart()

    inventory_page.click_shopping_cart_link()

    cart_page = CartPage(driver)

    cart_page.remove_item(driver)

    cart_page.is_cart_empty(driver)

    assert cart_page.is_cart_empty(driver) == [] , "Cart is empty"