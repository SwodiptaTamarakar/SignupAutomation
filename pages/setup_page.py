
import time, random

class SetupPage:
    def __init__(self, page):
        self.page = page
    
    def generate_email(self):
        timestamp = int(time.time())
        return f"swodi46+{timestamp}@gmail.com"
    
    def generate_phone(self):
        return "98" + str(random.randint(10000000, 99999999))
    
    def fill_account_details(self, first_name, last_name, password):
        email = self.generate_email()
        phone = self.generate_phone()

        self.page.get_by_role("textbox", name="First Name").fill(first_name)

        self.page.get_by_role("textbox", name="Last Name").fill(last_name)

        self.page.get_by_role("textbox", name="Email Address").fill(email)
        print("Email field value:",self.page.get_by_role("textbox",name="Email Address").input_value())

        self.page.get_by_role("textbox", name="Phone Number").fill(phone)

        self.page.locator("input[name='password']").fill(password)

        self.page.locator("input[name='confirmPassword']").fill(password)

        return email, phone

    def click_next(self):

        self.page.get_by_role("button", name="Next").click()