import pytest
from pages.signup_page import SignupPage
from pages.login_page import LoginPage

# Provide an instance of the pages for each test
@pytest.fixture
def signup_page(page):
    return SignupPage(page)

@pytest.fixture
def login_page(page):
    return LoginPage(page)