import allure
import requests
from allure_commons.types import Severity
from requests import Response

from conftest import *
from pages.main_page import MainPage


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "irauchuvatova")
@allure.label('layer', 'UI')
@allure.feature("UI")
@allure.story("Пользователь входит в личный кабинет с зарегистированным email")
@allure.link("https://litres.ru", name="Главная страница Литрес")
class TestLogin:
    endpoint = '/auth/register'
    @allure.title("Успешный логин")
    def test_success_login(self, browser_setup, endpoint=endpoint):
        with allure.step("Регистрация пользователя через API"):
            result: Response = requests.post(url=API_URL + endpoint,
                                             json={"email": EMAIL, "password": PASSWORD,
                                                   "mail_subscriptions_allowed": True})
        main_page = MainPage()
        with allure.step("Открыть главную страницу"):
            main_page.open()
        # WHEN
        with allure.step("Нажать кнопку Войти в навбаре"):
            main_page.click_login_on_navbar()
        with allure.step("Заполнить email на модальном окне Войти"):
            main_page.fill_email(EMAIL)
        with allure.step("Нажать на Продолжить на модальном окне Войти"):
            main_page.click_continue()
        with allure.step("Заполнить пароль на модальном окне Ввести пароль"):
            main_page.fill_password_for_login(PASSWORD)
        with allure.step("Нажать Войти на модальном окне Ввести пароль"):
            main_page.click_enter_on_modal()
            main_page.close_authorization_popup_close_button()
        # THEN
        with allure.step("Появление кнопки Профиль"):
            main_page.should_be_visible_button_profile()

    @allure.title("Логин с неправильным паролем")
    def test_unsuccess_login_wrong_password(self, browser_setup, endpoint=endpoint):
        with allure.step("Регистрация пользователя через API"):
            result: Response = requests.post(url=API_URL + endpoint,
                                             json={"email": EMAIL, "password": PASSWORD,
                                                   "mail_subscriptions_allowed": True})
        main_page = MainPage()
        with allure.step("Открыть главную страницу"):
            main_page.open()
        # WHEN
        with allure.step("Нажать кнопку Войти в навбаре"):
            main_page.click_login_on_navbar()
        with allure.step("Заполнить email на модальном окне Войти"):
            main_page.fill_email(EMAIL)
        with allure.step("Нажать на Продолжить на модальном окне Войти"):
            main_page.click_continue()
        with allure.step("Заполнить пароль на модальном окне Ввести пароль"):
            main_page.fill_password_for_login(DIFFERENT_PASSWORD)
        with allure.step("Нажать Войти на модальном окне Ввести пароль"):
            main_page.click_enter_on_modal()
        # THEN
        with allure.step("Появление предупреждения о неправильном пароле"):
            main_page.should_be_error_wrong_password()
        with allure.step("Кнопка Профиль не появляется"):
            main_page.should_be_not_visible_button_profile()

    @allure.title("Логин без пароля")
    def test_unsuccess_login_without_password(self, browser_setup, endpoint=endpoint):
        with allure.step("Регистрация пользователя через API"):
            result: Response = requests.post(url=API_URL + endpoint,
                                             json={"email": EMAIL, "password": PASSWORD,
                                                   "mail_subscriptions_allowed": True})
        main_page = MainPage()
        with allure.step("Открыть главную страницу"):
            main_page.open()
        # WHEN
        with allure.step("Нажать кнопку Войти в навбаре"):
            main_page.click_login_on_navbar()
        with allure.step("Заполнить email на модальном окне Войти"):
            main_page.fill_email(EMAIL)
        with allure.step("Нажать на Продолжить на модальном окне Войти"):
            main_page.click_continue()
        with allure.step("Нажать Войти на модальном окне Ввести пароль"):
            main_page.click_enter_on_modal()
        # THEN
        with allure.step("Появление предупреждения о незаполненном пароле"):
            main_page.should_be_not_empty_password()
        with allure.step("Кнопка Профиль не появляется"):
            main_page.should_be_not_visible_button_profile()
