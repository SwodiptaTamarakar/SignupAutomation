import os

class VerificationPreferencesPage:

    def __init__(self, page):
        self.page = page

    def fill_business_registration(self, number):
        self.page.get_by_role("textbox", name="Business Registration Number").fill(str(number))

    def select_country(self, country="Nepal"):
        self.page.get_by_role("combobox",name="Preferred Countries").click()

        self.page.wait_for_timeout(1000)

        print(self.page.get_by_text(country,exact=True).count())

        self.page.get_by_text(country, exact=True).nth(0).click()

    def select_services(self):
        self.page.get_by_role("checkbox", name="Colleges").click()
        self.page.get_by_role("checkbox", name="Vocational School").click()

    def fill_certification(self, text):
        self.page.get_by_role("textbox", name="Certification Details (").fill(text)

    def upload_file(self, file_name):
        file_path = os.path.abspath(file_name)
        self.page.set_input_files("input[type='file']", file_path)

    def submit(self):
        self.page.get_by_role("button", name="Submit").click()
