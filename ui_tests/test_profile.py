import allure
import requests
from allure_commons.types import Severity
from requests import Response
from selene import browser, have
from conftest import *
from pages.main_page import MainPage
from pages.profile_page import ProfilePage


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "irauchuvatova")
@allure.feature("Задачи в репозитории")
@allure.story("Зарегистрированный и авторизованный пользователь входит в профиль")
@allure.link("https://litres.ru", name="Главная страница Литрес")
class TestLogin:

    @allure.title("Успешный переход в профиль")
    def test_redirect_to_profile(browser_setup):
        main_page = MainPage()
        with allure.step("Регистрация пользователя через API"):
            result: Response = requests.post(url=API_URL_REGISTER,
                                             json={"email": EMAIL, "password": PASSWORD,
                                                   "mail_subscriptions_allowed": True})
        with allure.step("Логин пользователя через API"):
            result: Response = requests.post(url=API_URL_LOGIN,
                                             json={"login": EMAIL, "password": PASSWORD})

        with allure.step("Получить cookie из API"):
            payload = result.json().get('payload')
            data = payload.get('data')
            sid = data.get('sid')
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
        with allure.step("Открытие страницы Профиль"):
            browser.element(".Avatar-module__topContent_3OnBY").should(have.exact_text(
                NAME))
