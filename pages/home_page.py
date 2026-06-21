from playwright.sync_api import Page

class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.click_button = self.page.get_by_role("link", name="Get Started")

    def click_get_started(self):
        self.click_button.click()