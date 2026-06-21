class ProfessionalExperiencePage:

    def __init__(self, page):
        self.page = page

    def select_years_experience(self, years="3 years"):
        self.page.get_by_role("combobox", name="Years of Experience").click()
        self.page.get_by_role("option", name=years).click()

    def fill_students_recruited(self, value):
        self.page.get_by_role("spinbutton", name="Number of Students Recruited").fill(str(value))

    def fill_focus_area(self, text):
        self.page.get_by_role("textbox", name="Focus Area").fill(text)

    def fill_success_metrics(self, value):
        if int(value) > 100:
            raise ValueError("Success Metrics cannot exceed 100")
        self.page.get_by_role("spinbutton", name="Success Metrics").fill(str(value))

    def select_services(self):
        self.page.get_by_role("checkbox", name="Admission Applications").click()
        self.page.get_by_role("checkbox", name="Career Counseling").click()

    def click_next_bottom(self):
        self.page.get_by_role("button", name="Next").click()