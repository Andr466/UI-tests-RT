from pages.auth_page import AuthPage


def test_auth_by_email(web_browser):
    "Authorization by email with valid data"

    page = AuthPage(web_browser)
    page.btn_mail.click()
    page.username.send_keys('valid_data')
    page.password.send_keys('valid_data')
    page.btn_log.click()

    assert 'https://b2c.passport.rt.ru/account_b2c' in page.get_current_url()


def test_auth_by_phone(web_browser):
    "Authorization by phone number with valid data"

    page = AuthPage(web_browser)
    page.btn_phone.click()
    page.username.send_keys('valid_data')
    page.password.send_keys('valid_data')
    page.btn_log.click()

    assert 'https://b2c.passport.rt.ru/account_b2c' in page.get_current_url()


def test_auth_by_login(web_browser):
    "Authorization by login with valid data"

    page = AuthPage(web_browser)
    page.btn_login.click()
    page.username.send_keys('valid_data')
    page.password.send_keys('valid_data')
    page.btn_log.click()

    assert 'https://b2c.passport.rt.ru/account_b2c' in page.get_current_url()


def test_auth_by_ls(web_browser):
    "Authorization by personal account with valid data"

    page = AuthPage(web_browser)
    page.btn_ls.click()
    page.username.send_keys('valid_data')
    page.password.send_keys('valid_data')
    page.btn_log.click()

    assert 'https://b2c.passport.rt.ru/account_b2c' in page.get_current_url()


def test_auth_by_email_with_invalid_data(web_browser):
    "Authorization by email with invalid data"

    page = AuthPage(web_browser)
    page.btn_mail.click()
    page.username.send_keys('invalid_data')
    page.password.send_keys('invalid_data')
    page.btn_log.click()

    assert 'https://b2c.passport.rt.ru/account_b2c' in page.get_current_url(), "Login error. Wrong email or password."


def test_auth_by_phone_with_invalid_data(web_browser):
    "Authorization by phone with invalid data"

    page = AuthPage(web_browser)
    page.btn_phone.click()
    page.username.send_keys('invalid_data')
    page.password.send_keys('invalid_data')
    page.btn_log.click()

    assert 'https://b2c.passport.rt.ru/account_b2c' in page.get_current_url(), "Login error. Wrong phone or password."


def test_auth_by_login_with_invalid_data(web_browser):
    "Authorization by login with invalid data"

    page = AuthPage(web_browser)
    page.btn_login.click()
    page.username.send_keys('invalid_data')
    page.password.send_keys('invalid_data')
    page.btn_log.click()

    assert 'https://b2c.passport.rt.ru/account_b2c' in page.get_current_url(), "Login error. Wrong login or password."


def test_auth_by_ls_with_invalid_data(web_browser):
    "Authorization by personal account with invalid data"

    page = AuthPage(web_browser)
    page.btn_ls.click()
    page.username.send_keys('invalid_data')
    page.password.send_keys('invalid_data')
    page.btn_log.click()

    assert 'https://b2c.passport.rt.ru/account_b2c' in page.get_current_url(), "Login error. Wrong personal account or password."


def test_auth_by_vk(web_browser):
    "Possibility of authorization by a social network VK"
    page = AuthPage(web_browser)
    page.ic_vk.click()

    assert 'https://id.vk.com/auth' in page.get_current_url()


def test_auth_by_ok(web_browser):
    "Possibility of authorization by a social network OK"
    page = AuthPage(web_browser)
    page.ic_ok.click()

    assert 'https://connect.ok.ru/dk' in page.get_current_url()


def test_auth_by_mail(web_browser):
    "Possibility of authorization by a social network Mail"
    page = AuthPage(web_browser)
    page.ic_mail.click()

    assert 'https://connect.mail.ru/oauth/authorize' in page.get_current_url()


def test_auth_by_yandex(web_browser):
    "Possibility of authorization by a social network Yandex"
    page = AuthPage(web_browser)
    page.ic_ya.click()

    assert 'https://passport.yandex.ru/auth' in page.get_current_url()
    # BUG!!! https://docs.google.com/spreadsheets/d/1rIHhLucumtNI6VKTiilHWhvUyebLce2JWMBOCV7U4b0/edit#gid=0&range=A4
