import re
from playwright.sync_api import expect
from pages.base_page import BasePage
from data.constants import AppConfig

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.join_now_button = self.page.get_by_role("link", name="Join now")

    def open(self):
        self.page.goto("/en/login/")
        expect(self.page).to_have_url(f"{AppConfig.auth_url}/en/")

    def navigateToSignUp(self):
        self.join_now_button.click()
        expect(self.page).to_have_url(f"{AppConfig.auth_url}/en/signup")