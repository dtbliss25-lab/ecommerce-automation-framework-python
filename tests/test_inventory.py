from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


def test_add_to_cart(driver, users_data ):

    CART_ITEM = (By.CLASS_NAME, "inventory_item_name")
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

    assert cart_page.is_item_displayed(CART_ITEM) is True, "Item is added to Cart"


def test_product_sort(driver, users_data):

    text ="Name (A to Z)"
    PRODUCT_ELEMENTS = (By.ID, "inventory_container")

    login_page = LoginPage(driver)

    driver.get("https://www.saucedemo.com")

    user = users_data["valid_user"]

    login_page.login(
        user["username"],
        user["password"]
    )

    inventory_page = InventoryPage(driver)

    inventory_page.select_product_sort(driver, text)

    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(PRODUCT_ELEMENTS)
    )

    actual_names = [element.strip() for element in PRODUCT_ELEMENTS if element.strip()]

    assert actual_names == sorted(actual_names, key=str.lower), \
        f"Inventory table not sorting A to Z. Current layout order: {actual_names}"














