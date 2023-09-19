import pytest
from playwright.sync_api import Page, expect
from pages.home import HomePage
# page = browser.new_page()
# home_page = HomePage(Page)

@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page: Page, home_page: HomePage) -> None:
    print("beforeEach")
    # Go to the starting url before each test.
    home_page.navigate()
    # page.goto("https://www.automationexercise.com/")
    yield
    print("afterEach")

def test_that_home_page_is_visible_successfully(page: Page) -> None:
    # Assertions url
    expect(page).to_have_url("https://www.automationexercise.com/")

# def test_that_New_User_Signup_is_visible(page: Page):
#     # Click on 'Signup / Login' button
#     home_page = HomePage(Page)
#     home_page.clickOnSignIn()