class HomePage:
    def __init__(self, page):
        self.page = page
        self.signin_btn = page.locator('[aria-label="Enter your search term"]')
    
    def navigate(self):
        self.page.goto("https://www.automationexercise.com/")

    def clickOnSignIn(self):
        self.signin_btn.click()