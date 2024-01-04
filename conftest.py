'''import os

import pytest
from dotenv import load_dotenv
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utils import attach

@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()
@pytest.fixture(scope='function')
def setup_browser(request):
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

    yield browser

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()
'''

import pytest
from selene.support.shared import browser
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import random
import string

options = Options()
options.add_argument("--remote-debugging-port=9222")
driver = webdriver.Chrome(options=options)
browser.config.driver = driver


def random_char(char_num):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(char_num))


NAME = random_char(7)
EMAIL = NAME + "@gmail.com"
PASSWORD = NAME + "1"
DIFFERENT_PASSWORD = PASSWORD + "!"
API_URL = 'https://api.litres.ru/foundation/api'
API_URL_REGISTER = API_URL + '/auth/register'
API_URL_LOGIN = API_URL + '/auth/login'


@pytest.fixture(scope='session', autouse=True)
def browser_setup():
    browser.config.base_url = 'https://www.litres.ru'
    browser.config.set_value_by_js = True
    browser.config.timeout = 2.0
    browser.config.window_width = 1400
    browser.config.window_height = 1200
    yield
    browser.quit()
