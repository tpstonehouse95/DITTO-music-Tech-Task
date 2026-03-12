from playwright.sync_api import expect
from data.constants import AppConfig

def test_password_minimum_length_validation(signup_page):
    # 1. Open the signup page
    signup_page.open()

    # 2. Assert miniumum password length (6 characters) is enforced
    signup_page.email_address_field.fill("testuser@gmail.com")
    signup_page.password_field.fill("12345")
    signup_page.email_address_field.click() # Trigger blur
    expect(signup_page.password_length_warning).to_be_visible()
    expect(signup_page.signup_button).to_be_disabled()
    signup_page.password_field.fill("123456")
    
    # 3. Assert signup is re-enabled after meeting minumum password length
    expect(signup_page.password_length_warning).not_to_be_visible()
    expect(signup_page.signup_button).to_be_enabled()