from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "Link is incorrect"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL), "Login form: Email is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), "Login form: Password is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_EMAIL), "Register form: Email is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTER_PASSWORD), "Register form: Password is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTER_PASSWORD_REPEAT), "Register form: Repeat password is not presented"