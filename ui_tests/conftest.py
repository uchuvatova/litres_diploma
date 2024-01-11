import os
import string
import random

import pytest
from dotenv import load_dotenv
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utils import attach


def random_char(char_num):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(char_num))


NAME = random_char(7)
EMAIL = NAME + "@rover.info"
PASSWORD = NAME + "1"
DIFFERENT_PASSWORD = PASSWORD + "!"
FOUR_SYMBOLS_PASSWORD = random_char(4)
API_URL = 'https://api.litres.ru/foundation/api'
API_URL_LOGIN = API_URL + '/auth/login'
API_RECOMMENDED = API_URL + '/arts/personal-recommendations'


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function')
def browser_setup(request):
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)
    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')
    driver = webdriver.Remote(command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
                              options=options)
    browser.config.driver = driver
    browser.config.base_url = 'https://www.litres.ru'
    browser.config.window_height = 1920
    browser.config.window_width = 1800

    yield browser

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()


