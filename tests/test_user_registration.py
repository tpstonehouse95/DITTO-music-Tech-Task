from data.user_factory import UserFactory

def test_signup_flow(login_page, signup_page):
    # 1. Generate the unique user data
    new_user = UserFactory.create_test_user()

    # 2. Open the login page
    login_page.open()

    # 3. Navigate to the sign up page
    login_page.navigateToSignUp()

    # 4. Complete sign up
    signup_page.fill_registration_form(new_user)
    signup_page.accept_terms()
    signup_page.submit()

    # 5. Assert captcha appears after submitting the form
    signup_page.wait_for_captcha()