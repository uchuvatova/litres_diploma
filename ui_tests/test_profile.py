import allure
import requests
from allure_commons.types import Severity
from requests import Response
from selene import have
from ui_tests.conftest import *
from pages.main_page import MainPage


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "irauchuvatova")
@allure.label('layer', 'UI')
@allure.feature("UI")
@allure.story("Зарегистрированный и авторизованный пользователь входит в профиль")
@allure.link("https://litres.ru", name="Главная страница Литрес")
class TestProfile:
    endpoint = '/auth/register'
    @allure.title("Успешный переход в профиль")
    def test_redirect_to_profile(self, browser_setup, endpoint=endpoint):
        main_page = MainPage()
        with allure.step("Регистрация и логин пользователя через API"):
            registration: Response = requests.post(url=API_URL + endpoint,
                                             json={"email": EMAIL, "password": PASSWORD,
                                                   "mail_subscriptions_allowed": True})
        with allure.step("Логин пользователя через API"):
            login: Response = requests.post(url=API_URL_LOGIN,
                                             json={"login": EMAIL, "password": PASSWORD})

        with allure.step("Получить cookie SID из API"):
            sid = login.json().get('payload').get('data').get('sid')
        with allure.step("Передать cookie в браузер"):
            main_page.open()
            browser.driver.add_cookie({"name": "SID", "value": sid})
        with allure.step("Перезагрузить страницу"):
            browser.driver.refresh()
        # WHEN
        with allure.step("Нажать кнопку Профиль в навбаре"):
            main_page.close_authorization_popup_close_button()
            main_page.click_button_profile()
        # THEN
        with allure.step("Убедиться, что открыта страница профиля авторизованного пользователя"):
            browser.element(".Avatar-module__topContent_3OnBY").should(have.exact_text(
                NAME))
