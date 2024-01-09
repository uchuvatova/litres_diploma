import allure
from allure_commons.types import Severity

from conftest import PASSWORD, EMAIL, DIFFERENT_PASSWORD
from pages.main_page import MainPage


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "irauchuvatova")
@allure.label('layer', 'UI')
@allure.feature("Задачи в репозитории")
@allure.story("Пользователь регистируется с новым email")
@allure.link("https://litres.ru", name="Главная страница Литрес")
class TestRegistration:
    endpoint = '/auth/register'
    @allure.title("Успешная регистрация")
    def test_success_registration(self, browser_setup):
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
        with allure.step("Отметить чекбокс с согласием на модальном окне Создать профиль"):
            main_page.checkbox_agree_on_modal()
        with allure.step("Нажать на Продолжить на модальном окне Создать профиль"):
            main_page.click_continue_after_email()
        with allure.step("Заполнить пароль"):
            main_page.fill_password(PASSWORD)
        with allure.step("Повторить пароль"):
            main_page.repeat_password(PASSWORD)
        with allure.step("Нажать Сохранить на модальном окне Задать пароль"):
            main_page.click_enter_on_modal()
        # THEN
        with allure.step("Появление кнопки Профиль"):
            main_page.should_be_visible_button_profile()

    @allure.title("Регистрация с отличающимися паролями")
    def test_registration_with_different_password(self, browser_setup):
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
        with allure.step("Отметить чекбокс с согласием на модальном окне Создать профиль"):
            main_page.checkbox_agree_on_modal()
        with allure.step("Нажать на Продолжить на модальном окне Создать профиль"):
            main_page.click_continue_after_email()
        with allure.step("Заполнить пароль"):
            main_page.fill_password(PASSWORD)
        with allure.step("Ввести отличающийся пароль"):
            main_page.repeat_password(DIFFERENT_PASSWORD)
        with allure.step("Нажать Сохранить на модальном окне Задать пароль"):
            main_page.click_enter_on_modal()
        # THEN
        with allure.step("Появление предупреждения, что пароли должны совпадать"):
            main_page.should_be_error_different_password()
        with allure.step("Кнопка Профиль не появляется"):
            main_page.should_be_not_visible_button_profile()

    @allure.title("Регистрация без пароля")
    def test_registration_without_password(self, browser_setup):
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
        with allure.step("Отметить чекбокс с согласием на модальном окне Создать профиль"):
            main_page.checkbox_agree_on_modal()
        with allure.step("Нажать на Продолжить на модальном окне Создать профиль"):
            main_page.click_continue_after_email()
        with allure.step("Нажать Сохранить на модальном окне Задать пароль"):
            main_page.click_enter_on_modal()
        # THEN
        with allure.step("Появление предупреждения Введите пароль"):
            main_page.should_be_not_empty_password()
        with allure.step("Кнопка Профиль не появляется"):
            main_page.should_be_not_visible_button_profile()
