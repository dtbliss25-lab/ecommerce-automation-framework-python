from conftest import users_data
from pages import login_page
from pages.login_page import LoginPage


def test_valid_login(driver, users_data):

    login_page = LoginPage(driver)

    driver.get("https://www.saucedemo.com")

    user = users_data["valid_user"]

    login_page.login(
        user["username"],
        user["password"]
    )

    assert "inventory" in driver.current_url


def test_invalid_login(driver, users_data):

    login_page = LoginPage(driver)

    driver.get("https://www.saucedemo.com")

    user = users_data["invalid_user"]

    login_page.login(
        user["username"],
        user["password"]
    )

    error = login_page.get_error_message()

    assert "Username and password do not match" in error

def test_locked_user(driver, users_data):

    login_page = LoginPage(driver)

    driver.get("https://www.saucedemo.com")

    user = users_data["locked_user"]

    login_page.login(
        user["username"],
        user["password"]
    )

    error = login_page.get_error_message()

    assert  "Epic sadface" in error

def test_empty_login(driver, users_data):

    login_page = LoginPage(driver)

    driver.get("https://www.saucedemo.com")

    login_page.click_login()

    error = login_page.get_error_message()

    assert "Epic sadface" in error