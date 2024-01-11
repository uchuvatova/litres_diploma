from selene import browser
from selene.support.conditions import be, have


class MainPage:
    def __init__(self):
        pass

    def open(self):
        browser.open("/")

    def click_login_on_navbar(self):
        browser.element('[href="/pages/login/"]').click()

    def fill_email(self, email):
        browser.element('#modal [name=email]').should(be.blank).type(email)

    def checkbox_agree_on_modal(self):
        browser.element('#modal .Checkbox__label_2hlWt').click()

    def fill_password(self, password):
        browser.element('#modal [name=regPwd]').should(be.blank).type(password)

    def fill_password_for_login(self, password):
        browser.element('#modal [name=pwd]').should(be.blank).type(password)

    def repeat_password(self, password):
        browser.element('#modal [name=regPwdRepeat]').should(be.blank).type(password)

    def click_continue(self):
        browser.element('#modal [type=submit]').click()

    def click_continue_after_email(self):
        browser.element('#modal [type=button]').click()

    def click_enter_on_modal(self):
        browser.element('#modal [type=submit]').click()

    def should_be_visible_button_profile(self):
        browser.element('[data-testid=header__profile-button]').should(be.visible)

    def click_button_profile(self):
        browser.element('[data-testid=header__profile-button]').click()

    def should_be_not_visible_button_profile(self):
        browser.element('[data-testid=header__profile-button]').should(be.not_.visible)

    def should_be_error_different_password(self):
        browser.element('.ControlInput-module__input__error_2jXOB').should(have.exact_text(
            "Пароли должны быть одинаковыми"))

    def should_be_not_empty_password(self):
        browser.element('.ControlInput-module__input__error_2jXOB').should(have.exact_text(
            "Введите пароль"))

    def should_be_error_wrong_password(self):
        browser.element('.ControlInput-module__input__error_2jXOB').should(have.exact_text(
            "Неверное сочетание логина и пароля"))

    def should_be_error_long_password(self):
        browser.element('.ControlInput-module__input__error_2jXOB').should(have.exact_text(
            "Введите не больше 100 символов"))

    def close_authorization_popup_close_button(self):
        browser.element('[data-test-id=authorization-popup__close-button]').click()
