from playwright.sync_api import Page, expect

from conftest import page

class TermsPage:
    def __init__(self, page: Page):
        self.page = page
    
    def accept_terms(self):
        self.page.get_by_role("checkbox", name="I agree to the Terms of").click()

        self.page.get_by_role("button", name="Continue").click()
        expect(self.page.get_by_text("Provide your personal details.")).to_be_visible()

    
