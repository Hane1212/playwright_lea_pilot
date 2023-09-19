from playwright.sync_api import Page

class HomePage:
    URL = 'https://www.automationexercise.com/'
    def __init__(self, page:Page) -> None:
        self.page = page
        # self.signin_btn = page.locator('[aria-label="Enter your search term"]')
    
    def navigate(self) -> None:
        print(self.URL)
        self.page.goto(self.URL)

    def clickOnSignIn(self):
        link = self.page.locator('//ul[@class="nav navbar-nav"]/li')
        for links in link.element_handles():
            linkF = links.get_attribute('href')
            if linkF == "/login":
                links.click()
            print(linkF)