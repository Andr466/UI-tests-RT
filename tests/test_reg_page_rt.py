from pages.reg_page import RegPage


def test_reg_form(web_browser):
    "Registration with valid data"

    page = RegPage(web_browser)
    page.btn_reg.click()
    page.first_name.send_keys('valid_data')
    page.last_name.send_keys('valid_data')
    page.email.send_keys('valid_data')
    page.password.send_keys('valid_data')
    page.pass_conf.send_keys('valid_data')
    page.btn_register.click()

    assert page.code.is_visible()  # Checking that the data has been accepted and the code entry window has opened


def test_reg_with_wrong_firstname_lastname(web_browser):
    page = RegPage(web_browser)
    page.btn_reg.click()
    page.first_name.send_keys('invalid_data')
    page.last_name.send_keys('invalid_data')
    page.email.send_keys('valid_data')
    page.password.send_keys('valid_data')
    page.pass_conf.send_keys('valid_data')
    page.btn_register.click()

    assert not page.msg1.is_visible() and not page.msg2.is_visible(), "Error in the first or last name input field." \
                                                                      "It is necessary to fill in the field in Cyrillic. From 2 to 30 characters."


def test_reg_with_wrong_email_or_number(web_browser):
    page = RegPage(web_browser)
    page.btn_reg.click()
    page.first_name.send_keys('valid_data')
    page.last_name.send_keys('valid_data')
    page.email.send_keys('invalid_data')
    page.password.send_keys('valid_data')
    page.pass_conf.send_keys('valid_data')
    page.btn_register.click()

    assert not page.msg3.is_visible(), "Enter the phone number in the format +7XXXXXXXXXXXX or +375XXXXXXXXX," \
                                       "or email in the format example@email.ru"


def test_reg_with_wrong_password(web_browser):
    page = RegPage(web_browser)
    page.btn_reg.click()
    page.first_name.send_keys('valid_data')
    page.last_name.send_keys('valid_data')
    page.email.send_keys('valid_data')
    page.password.send_keys('invalid_data')
    page.pass_conf.send_keys('invalid_data')
    page.btn_register.click()

    assert not page.msg4.is_visible() and not page.msg5.is_visible(), "The password must be at least 8 and no more than 20 characters long. " \
                                                                      "The password must contain only Latin letters, at least one uppercase and " \
                                                                      "lowercase letters, at least 1 special character or at least one digit"


def test_reg_with_different_passwords(web_browser):
    page = RegPage(web_browser)
    page.btn_reg.click()
    page.first_name.send_keys('valid_data')
    page.last_name.send_keys('valid_data')
    page.email.send_keys('valid_data')
    page.password.send_keys('valid_data')
    page.pass_conf.send_keys('diff_valid_data')
    page.btn_register.click()

    assert not page.msg5.is_visible(), "Passwords don't match"


def test_reg_with_registered_account(web_browser):
    """Registration with an existing account with a transition to the authorization page"""

    page = RegPage(web_browser)
    page.btn_reg.click()
    page.first_name.send_keys('valid_data')
    page.last_name.send_keys('valid_data')
    page.email.send_keys('auth_valid_data')
    page.password.send_keys('valid_data')
    page.pass_conf.send_keys('valid_data')
    page.btn_register.click()

    assert page.window.is_visible()

    page.btn_window_log.click()

    assert 'https://b2c.passport.rt.ru/auth' in page.get_current_url()


def test_reg_with_registered_account_2(web_browser):
    """Registration with an existing account with a transition to the password recovery page"""

    page = RegPage(web_browser)
    page.btn_reg.click()
    page.first_name.send_keys('valid_data')
    page.last_name.send_keys('valid_data')
    page.email.send_keys('auth_valid_data')
    page.password.send_keys('valid_data')
    page.pass_conf.send_keys('valid_data')
    page.btn_register.click()

    assert page.window.is_visible()

    page.btn_rec_pass.click()

    assert 'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions' in page.get_current_url()
