from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import BasePageLocators
import time

class LoginPage(BasePage):
    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, "It's not a login page"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.SIGN_IN), 'No login form'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.SIGN_UP), 'No registration form'

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented, probably unauthorised user"
    
    def register_new_user(self):
        email = self.browser.find_element(*LoginPageLocators.SIGN_UP_EMAIL)
        email.click().send_keys(str(time.time()) + "@fakemail.org")

        pas = self.browser.find_element(*LoginPageLocators.SIGN_UP_PASS)
        pas.click().send_keys(str(time.time()) + 'ChuBaKa')

        pas_confirm = self.browser.find_element(*LoginPageLocators.SIGN_UP_PASS_CONFIRM)
        pas_confirm.click().send_keys(str(time.time()) + 'ChuBaKa')

        self.browser.find_element(*LoginPageLocators.SIGN_UP_BUTTON).click()