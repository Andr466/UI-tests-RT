from pages.pass_recovery_page import PassRecPage
import time


def test_pass_rec_form_by_mail(web_browser):
    page = PassRecPage(web_browser)
    page.btn_pass.click()
    page.btn_mail.click()
    page.username.send_keys('valid_data')

    # Stopping program execution for manual captcha entry
    time.sleep(10)

    page.btn_reset.click()

    assert page.code.is_visible()


def test_pass_rec_form_by_phone(web_browser):
    page = PassRecPage(web_browser)
    page.btn_pass.click()
    page.btn_phone.click()
    page.username.send_keys('valid_data')

    # Stopping program execution for manual captcha entry
    time.sleep(10)

    page.btn_reset.click()

    assert page.code.is_visible()


def test_pass_rec_form_by_login(web_browser):
    page = PassRecPage(web_browser)
    page.btn_pass.click()
    page.btn_login.click()
    page.username.send_keys('valid_data')

    # Stopping program execution for manual captcha entry
    time.sleep(10)

    page.btn_reset.click()

    assert page.code.is_visible()


def test_pass_rec_form_by_ls(web_browser):
    page = PassRecPage(web_browser)
    page.btn_pass.click()
    page.btn_ls.click()
    page.username.send_keys('valid_data')

    # Stopping program execution for manual captcha entry
    time.sleep(10)

    page.btn_reset.click()

    assert page.code.is_visible()


def test_btn_go_back_auth(web_browser):
    page = PassRecPage(web_browser)
    page.btn_pass.click()
    page.btn_go_back.click()

    assert 'https://b2c.passport.rt.ru/auth' in page.get_current_url()
