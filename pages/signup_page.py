import re
from playwright.sync_api import expect
from pages.base_page import BasePage
from data.constants import AppConfig
from data.user_factory import UserFactory

class SignupPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.email_address_field = self.page.get_by_role("textbox", name="Email Address")
        self.password_field = self.page.get_by_role("textbox", name="Password")
        self.agreement_checkbox = self.page.get_by_label('I have read and agree to')
        self.signup_button = self.page.get_by_role("button", name="Sign up")
        self.captcha_challenge = self.page.locator("iframe[title^='recaptcha challenge']:visible")
        self.password_length_warning = self.page.get_by_text("Your password must be at least 6 characters long")

    def open(self):
        self.page.goto(f"{AppConfig.auth_url}/en/signup/")
        expect(self.page).to_have_url(f"{AppConfig.auth_url}/en/signup/")

    def fill_registration_form(self, user):
        self.email_address_field.fill(user.email)
        self.password_field.fill(user.password)

    def accept_terms(self):
        self.agreement_checkbox.check(force=True)
    
    def submit(self):
        self.signup_button.click()

    def wait_for_captcha(self):
        expect(self.captcha_challenge).to_be_visible(timeout=10000)