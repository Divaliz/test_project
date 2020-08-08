from .base_page import BasePage
from .locators import LoginPageLocators
import time

email = str(time.time()) + "@fakemail.org"
password = "pepegaclap"


class LoginPage(BasePage, LoginPageLocators):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.LOGIN_LINK == self.browser.current_url, "Invalid login link"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is missing"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is missing"

    def register_new_user(self):
        email_field = self.browser.find_element(*LoginPageLocators.EMAIL_ADDRESS_FIELD)
        email_field.send_keys(email)
        password_field1 = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD)
        password_field1.send_keys(password)
        confirm_password = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD_FIELD)
        confirm_password.send_keys(password)
        register_btn = self.browser.find_element(*LoginPageLocators.REGISTER_BTN)
        register_btn.click()
