import random
import string

import requests

from litres_diploma_tests.utils.users import User


def random_char(char_num):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(char_num))


NAME = random_char(7)
EMAIL = NAME + "@rover.info"
PASSWORD = NAME + "1"
DIFFERENT_PASSWORD = PASSWORD + "!"
FOUR_SYMBOLS_PASSWORD = random_char(4)
LONG_PASSWORD = random_char(101)
API_URL = 'https://api.litres.ru/foundation/api'
API_URL_LOGIN = API_URL + '/auth/login'
API_RECOMMENDED = API_URL + '/arts/personal-recommendations'
mail_subscriptions_allowed = [True, False]


# for UI tests
def registration_user_for_ui_login():
    requests.post(url=f'{API_URL}/auth/register',
                  json={"email": EMAIL,
                        "password": PASSWORD,
                        "mail_subscriptions_allowed": random.choice(mail_subscriptions_allowed)})


user_to_registrate_ui = User(email=random_char(7) + "@rover.info", password=random_char(7) + "!")
user_to_registrate_diff_pass_ui = User(email=random_char(7) + "@rover.info", password=random_char(7) + "!")
user_to_registrate_without_pass_ui = User(email=random_char(7) + "@rover.info", password=random_char(7) + "!")
user_to_registrate_with_long_password_ui = User(email=random_char(7) + "@rover.info", password=random_char(101))


# for API tests
def new_user_for_api():
    new_user = {
        "email": EMAIL,
        "password": PASSWORD,
        "mail_subscriptions_allowed": random.choice(mail_subscriptions_allowed)}
    return new_user


def new_user_with_short_password_for_api():
    new_user = {"email": EMAIL,
                "password": FOUR_SYMBOLS_PASSWORD,
                "mail_subscriptions_allowed": random.choice(mail_subscriptions_allowed)}
    return new_user
