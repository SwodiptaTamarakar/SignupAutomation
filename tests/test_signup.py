import time
from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.terms_page import TermsPage
from pages.setup_page import SetupPage
from pages.otp_page import OTPPage
from utils.gmail import GmailReader
from pages.agency_page import AgencyDetailsPage
from pages.professional_page import ProfessionalExperiencePage
from pages.verification_page import VerificationPreferencesPage


def test_signup(page: Page):

    page.goto("https://authorized-partner.vercel.app/", timeout=60000)

    home_page = HomePage(page)
    terms = TermsPage(page)
    account = SetupPage(page)
    otp_page = OTPPage(page)
    agency = AgencyDetailsPage(page)
    prof = ProfessionalExperiencePage(page)
    verify = VerificationPreferencesPage(page)

    home_page.click_get_started()
    terms.accept_terms()

    generated_email, phone = account.fill_account_details(first_name="Swodipta", last_name="Tamrakar", password="Swodipta123@")

    print("Generated email:", generated_email)
    print("Generated phone:", phone)

    account.click_next()

    print("Waiting for OTP page...")
    page.wait_for_timeout(3000)

    gmail = GmailReader(gmail_user="swodi46@gmail.com", app_password="lfgflclxdxuniecx")

    print("Current time:", time.ctime())

    otp = gmail.get_otp(generated_email, timeout=120)

    print("OTP RECEIVED =", otp)

    print("Input count:",
          page.locator("input").count())

    otp_page.enter_otp(otp)

    page.wait_for_timeout(1000)

    otp_page.verify()

    page.wait_for_timeout(3000)

    print("Current URL:", page.url)

    expect(page.locator("text=Agency Details")).to_be_visible()

    agency.fill_agency_details(
        agency_name="Global Travels",
        role="Manager",
        agency_email="contact@globaltravels.com",
        website="www.globaltravels.com",
        address="Kathmandu",
        region="Nepal"
    )

    agency.click_next()

    prof.select_years_experience("3 years")
    prof.fill_students_recruited(98)
    prof.fill_focus_area("Nepal")
    prof.fill_success_metrics(93)

    prof.select_services()
    prof.click_next_bottom()

    verify.fill_business_registration("23456")

    page.screenshot(path="verification_page.png")
    verify.select_country("Nepal")

    verify.select_services()

    verify.fill_certification("IEEC Certified")

    verify.upload_file("files/swodipta-tamarkar (1).pdf")

    verify.submit()

    print("Signup completed successfully")