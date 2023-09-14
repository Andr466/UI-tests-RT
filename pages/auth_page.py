from pages.base import WebPage
from pages.elements import WebElement


class AuthPage(WebPage):

    def __init__(self, web_driver, url=''):
        url = 'https://b2c.passport.rt.ru/auth'
        super().__init__(web_driver, url)

    username = WebElement(id='username')
    password = WebElement(id='password')
    btn_log = WebElement(id='kc-login')
    btn_phone = WebElement(id='t-btn-tab-phone')
    btn_mail = WebElement(id='t-btn-tab-mail')
    btn_login = WebElement(id='t-btn-tab-login')
    btn_ls = WebElement(id='t-btn-tab-ls')
    btn_forgot_pass = WebElement(id='forgot_password')
    btn_reg = WebElement(id='kc-register')
    ic_vk = WebElement(id='oidc_vk')
    ic_ok = WebElement(id='oidc_ok')
    ic_mail = WebElement(id='oidc_mail')
    ic_ya = WebElement(id='oidc_ya')
