import time

class AgencyDetailsPage:

    def __init__(self, page):
        self.page = page

    def fill_agency_details(self, agency_name, role, agency_email, website, address, region):

        self.page.get_by_role("textbox", name="Name").fill(agency_name)

        self.page.get_by_role("textbox", name="Role in Agency").fill(role)

        self.page.get_by_role("textbox", name="Email Address").fill(agency_email)

        self.page.get_by_role("textbox", name="Website").fill(website)

        self.page.get_by_role("textbox", name="Address", exact=True).fill(address)

        self.page.get_by_role("combobox").click()

        self.page.get_by_text(region).click()

    def click_next(self):
        self.page.get_by_role("button", name="Next").click()