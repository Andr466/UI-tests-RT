from pages.base import WebPage
from pages.elements import WebElement


class PassRecPage(WebPage):

    def __init__(self, web_driver, url=''):
        url = 'https://b2c.passport.rt.ru/auth'
        super().__init__(web_driver, url)

    btn_pass = WebElement(id='forgot_password')
    btn_phone = WebElement(id='t-btn-tab-phone')
    btn_mail = WebElement(id='t-btn-tab-mail')
    btn_login = WebElement(id='t-btn-tab-login')
    btn_ls = WebElement(id='t-btn-tab-ls')
    username = WebElement(id='username')
    captcha = WebElement(id='captcha')
    btn_reset = WebElement(id='reset')
    btn_go_back = WebElement(id='reset-back')
    code = WebElement(id='rt-code-0')
