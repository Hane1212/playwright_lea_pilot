import pytest
from playwright.sync_api import Page, expect


@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page: Page):
    print("beforeEach")
    # Go to the starting url before each test.
    page.goto("https://www.automationexercise.com/")
    yield
    print("afterEach")

def test_that_home_page_is_visible_successfully(page: Page):
    # Assertions use the expect API.
    expect(page).to_have_url("https://www.automationexercise.com/")

def test_that_New_User_Signup_is_visible(page: Page):
    # Click on 'Signup / Login' button
    link = page.locator('//ul[@class="nav navbar-nav"]/li')
    for links in link.element_handles():
        linkF = links.get_attribute('href')
        print(linkF)
