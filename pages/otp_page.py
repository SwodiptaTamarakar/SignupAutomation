class OTPPage:

    def __init__(self, page):
        self.page = page

    def enter_otp(self, otp: str):
        self.page.locator("input").fill(otp)

    def verify(self):
        self.page.get_by_role("button", name="Verify Code").click()