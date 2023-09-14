from RT.page_rt.base import WebPage
from RT.page_rt.elements import WebElement


class RegPage(WebPage):

    def __init__(self, web_driver, url=''):
        url = 'https://b2c.passport.rt.ru/auth'
        super().__init__(web_driver, url)

    btn_reg = WebElement(id='kc-register')
    first_name = WebElement(name='firstName')
    last_name = WebElement(name='lastName')
    email = WebElement(id='address')
    password = WebElement(id='password')
    pass_conf = WebElement(id='password-confirm')
    btn_register = WebElement(name='register')
    code = WebElement(id='rt-code-0')
    # Error message in the first name input field
    msg1 = WebElement(xpath='//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/span[1]')
    # Error message in the last name input field
    msg2 = WebElement(xpath='//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/span[1]')
    # Error message in the email or phone input field
    msg3 = WebElement(xpath='//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[3]/div[1]/span[1]')
    # Error message in the password input field
    msg4 = WebElement(xpath='//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[4]/div[1]/span[1]')
    # Error message in the password confirmation input field
    msg5 = WebElement(xpath='//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[4]/div[2]/span[1]')
    window = WebElement(xpath='//*[@id="page-right"]/div/div/div/form/div[1]/div')
    btn_window_log = WebElement(name='gotoLogin')
    btn_rec_pass = WebElement(id='reg-err-reset-pass')
