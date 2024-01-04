import allure
from allure_commons.types import Severity

from conftest import PASSWORD, EMAIL, DIFFERENT_PASSWORD
from pages.main_page import MainPage


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "irauchuvatova")
@allure.feature("Задачи в репозитории")
@allure.story("Пользователь регистируется с новым email")
@allure.link("https://litres.ru", name="Главная страница Литрес")
class TestRegistration:

    @allure.title("Успешная регистрация")
    def test_success_registration(browser_management):
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
    def test_registration_with_different_password(browser_management):
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
    def test_registration_without_password(browser_management):
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

    '''with allure.step("Fill last name"):
        registration_page.fill_last_name('Uchuvatova')
    with allure.step("Choose hobby"):
        registration_page.choose_hobbies('Reading')
    with allure.step("Fill date of birth"):
        registration_page.fill_date_of_birth('1986', 'April', 26)
    with allure.step("Fill email"):
        registration_page.fill_email('example@mail.ru')
    with allure.step("Choose gender"):
        registration_page.choose_gender('Female')
    with allure.step("Fill phone"):
        registration_page.fill_phone('1234567890')
    with allure.step("Choose subjects"):
        registration_page.choose_subjects('Maths')
    with allure.step("Add photo"):
        registration_page.add_photo('resourses/1.png')
    with allure.step("Fill address"):
        registration_page.fill_address('Sunstreet, 28', 'NCR', 'Delhi')
    with allure.step("Submit form"):
        registration_page.submit()

    # THEN
    with allure.step("Check results"):
        registration_page.should_open_submit_form()
        registration_page.registered_user_data.should(
            have.exact_texts(
                "Ira Uchuvatova",
                "example@mail.ru",
                "Female",
                "1234567890",
                "26 April,1986",
                "Maths",
                "Reading",
                "1.png",
                "Sunstreet, 28",
                "NCR Delhi"))'''
