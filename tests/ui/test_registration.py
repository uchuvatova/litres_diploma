import allure
from allure_commons.types import Severity

from litres_diploma_tests.pages.web.main_page import MainPage
from litres_diploma_tests.utils.data import user_to_registrate_ui, \
    user_to_registrate_with_long_password_ui, user_to_registrate_diff_pass_ui, user_to_registrate_without_pass_ui


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "irauchuvatova")
@allure.label('layer', 'UI')
@allure.feature("UI")
@allure.story("Пользователь регистируется с новым email")
@allure.link("https://litres.ru", name="Главная страница Литрес")
class TestRegistration:
    @allure.title("Успешная регистрация")
    def test_success_registration(self, browser_setup):
        user = user_to_registrate_ui
        main_page = MainPage()
        with allure.step("Открыть главную страницу"):
            main_page.open()
        # WHEN
        with allure.step("Нажать кнопку Войти в навбаре"):
            main_page.click_login_on_navbar()
        with allure.step("Заполнить email на модальном окне Войти"):
            main_page.fill_email(user.email)
        with allure.step("Нажать на Продолжить на модальном окне Войти"):
            main_page.click_continue()
        with allure.step("Отметить чекбокс с согласием на модальном окне Создать профиль"):
            main_page.checkbox_agree_on_modal()
        with allure.step("Нажать на Продолжить на модальном окне Создать профиль"):
            main_page.click_continue_after_email()
        with allure.step("Заполнить пароль"):
            main_page.fill_password(user.password)
        with allure.step("Повторить пароль"):
            main_page.repeat_password(user.password)
        with allure.step("Нажать Сохранить на модальном окне Задать пароль"):
            main_page.click_enter_on_modal()
        # THEN
        with allure.step("Появление кнопки Профиль"):
            main_page.should_be_visible_button_profile()

    @allure.title("Регистрация с несовпадающими паролями")
    def test_registration_with_different_password(self, browser_setup):
        user = user_to_registrate_diff_pass_ui
        different_password = user.password + "!"
        main_page = MainPage()
        with allure.step("Открыть главную страницу"):
            main_page.open()
        # WHEN
        with allure.step("Нажать кнопку Войти в навбаре"):
            main_page.click_login_on_navbar()
        with allure.step("Заполнить email на модальном окне Войти"):
            main_page.fill_email(user.email)
        with allure.step("Нажать на Продолжить на модальном окне Войти"):
            main_page.click_continue()
        with allure.step("Отметить чекбокс с согласием на модальном окне Создать профиль"):
            main_page.checkbox_agree_on_modal()
        with allure.step("Нажать на Продолжить на модальном окне Создать профиль"):
            main_page.click_continue_after_email()
        with allure.step("Заполнить пароль"):
            main_page.fill_password(user.password)
        with allure.step("Ввести отличающийся пароль"):
            main_page.repeat_password(different_password)
        with allure.step("Нажать Сохранить на модальном окне Задать пароль"):
            main_page.click_enter_on_modal()
        # THEN
        with allure.step("Появление предупреждения, что пароли должны совпадать"):
            main_page.should_be_error_different_password()
        with allure.step("Кнопка Профиль не появляется"):
            main_page.should_be_not_visible_button_profile()

    @allure.title("Регистрация без пароля")
    def test_registration_without_password(self, browser_setup):
        user = user_to_registrate_without_pass_ui
        main_page = MainPage()
        with allure.step("Открыть главную страницу"):
            main_page.open()
        # WHEN
        with allure.step("Нажать кнопку Войти в навбаре"):
            main_page.click_login_on_navbar()
        with allure.step("Заполнить email на модальном окне Войти"):
            main_page.fill_email(user.email)
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
            main_page.should_be_error_empty_password()
        with allure.step("Кнопка Профиль не появляется"):
            main_page.should_be_not_visible_button_profile()

    @allure.title("Регистрация с паролем больше 100 символов")
    def test_registration_with_long_password(self, browser_setup):
        user = user_to_registrate_with_long_password_ui
        main_page = MainPage()
        with allure.step("Открыть главную страницу"):
            main_page.open()
        # WHEN
        with allure.step("Нажать кнопку Войти в навбаре"):
            main_page.click_login_on_navbar()
        with allure.step("Заполнить email на модальном окне Войти"):
            main_page.fill_email(user.email)
        with allure.step("Нажать на Продолжить на модальном окне Войти"):
            main_page.click_continue()
        with allure.step("Отметить чекбокс с согласием на модальном окне Создать профиль"):
            main_page.checkbox_agree_on_modal()
        with allure.step("Нажать на Продолжить на модальном окне Создать профиль"):
            main_page.click_continue_after_email()
        with allure.step("Заполнить пароль значением длиной > 100 символов"):
            main_page.fill_password(user.password)
        with allure.step("Повторить пароль значением длиной > 100 символов"):
            main_page.repeat_password(user.password)
        with allure.step("Нажать Сохранить на модальном окне Задать пароль"):
            main_page.click_enter_on_modal()
        # THEN
        with allure.step("Появление предупреждения Введите не больше 100 символов"):
            main_page.should_be_error_long_password()
        with allure.step("Кнопка Профиль не появляется"):
            main_page.should_be_not_visible_button_profile()
