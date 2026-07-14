from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from selenium.webdriver.support import expected_conditions as EC



def test_checkout(users_data, driver):

    FIRST_NAME = (By.ID, "first-name")

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

    cart_page.click_checkout()

    checkout_page = CheckoutPage(driver)

    WebDriverWait(driver, 5).until(
        EC.url_contains("checkout-step-one.html")
    )

    checkout_page.continue_checkout( driver,
        "John",
        "Smith",
        "3000"
    )

    checkout_page.click_finish()

    WebDriverWait(driver, 5).until(
        EC.url_contains("checkout-complete.html")
    )

    confirmation = checkout_page.get_confirmation_message()

    assert "Thank you" in confirmation
