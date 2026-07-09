from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


def test_empty_cart(users_data, driver):
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