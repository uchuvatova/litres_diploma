import json
import logging

import allure
import jsonschema
import pytest
import requests
from allure_commons.types import AttachmentType
from requests import Response

from litres_diploma_tests.utils.data import API_URL, PASSWORD, EMAIL, FOUR_SYMBOLS_PASSWORD, new_user_for_api, \
    new_user_with_short_password_for_api
from schemas.load_schema import SUCCESSFUL_REGISTER_USER_PATH, load_schema, REGISTER_EXIST_USER_PATH, \
    UNSUCCESSFUL_REGISTER_USER_PATH


@allure.epic('API регистрации')
@allure.story('Регистрация по email')
class TestRegistration:
    endpoint = '/auth/register'

    @pytest.fixture(scope='function')
    def exist_user(self, endpoint=endpoint):
        exist_user = new_user_for_api()

        requests.post(url=API_URL + endpoint, json=exist_user)
        return exist_user

    @allure.title('Успешная регистрация пользователя по email')
    @allure.feature('Регистрация по email')
    @allure.label('owner', 'irauchuvatova')
    @allure.label('layer', 'API')
    @allure.tag('smoke', 'regress', 'API', 'registration')
    @allure.severity('critical')
    def test_post_register_user_successful(self, endpoint=endpoint):
        schema = load_schema(SUCCESSFUL_REGISTER_USER_PATH)

        with allure.step('Создать нового пользователя'):
            new_user = new_user_for_api()
        with allure.step(f'Отправить POST-запрос на {endpoint} для регистрации нового пользователя'):
            result: Response = requests.post(url=API_URL + endpoint, json=new_user)

        with allure.step('Проверить, что API возвращает 201 код ответа'):
            assert result.status_code == 201
        with allure.step('Провалидировать схему ответа'):
            jsonschema.validate(result.json(), schema)

        allure.attach(body=result.request.url,
                      name="Request url",
                      attachment_type=AttachmentType.TEXT)
        allure.attach(body=result.request.method,
                      name="Request method",
                      attachment_type=AttachmentType.TEXT)
        allure.attach(body=result.request.body,
                      name="Request body",
                      attachment_type=AttachmentType.JSON,
                      extension="json")
        allure.attach(body=json.dumps(result.json(), indent=4, ensure_ascii=True),
                      name="Response body",
                      attachment_type=AttachmentType.JSON,
                      extension="json")
        logging.info(result.request.url)
        logging.info(result.status_code)
        logging.info(result.text)

    @allure.title('Неуспешная регистрация существующего пользователя по email')
    @allure.feature('Регистрация по email')
    @allure.label('owner', 'irauchuvatova')
    @allure.label('layer', 'API')
    @allure.tag('smoke', 'regress', 'API', 'registration')
    @allure.severity('critical')
    def test_post_register_exist_user_unsuccessful(self, exist_user, endpoint=endpoint):
        schema = load_schema(REGISTER_EXIST_USER_PATH)
        with allure.step('Создать нового пользователя, совпадающего с уже созданным'):
            user = exist_user

        with allure.step(f'Отправить POST-запрос на {endpoint} для регистрации существующего пользователя'):
            result: Response = requests.post(url=API_URL + endpoint, json=user)

        with allure.step('Проверить, что API возвращает 400 код ответа'):
            assert result.status_code == 400
        with allure.step('Провалидировать схему ответа'):
            jsonschema.validate(result.json(), schema)
        with allure.step('Проверить сообщение о существующем пользователе'):
            assert 'User already exists' in result.text

        allure.attach(body=result.request.url,
                      name="Request url",
                      attachment_type=AttachmentType.TEXT)
        allure.attach(body=result.request.method,
                      name="Request method",
                      attachment_type=AttachmentType.TEXT)
        allure.attach(body=result.request.body,
                      name="Request body",
                      attachment_type=AttachmentType.JSON,
                      extension="json")
        allure.attach(body=json.dumps(result.json(), indent=4, ensure_ascii=True),
                      name="Response body",
                      attachment_type=AttachmentType.JSON,
                      extension="json")
        logging.info(result.request.url)
        logging.info(result.status_code)
        logging.info(result.text)

    @allure.title('Неуспешная регистрация пользователя по email с паролем меньше 5 символов')
    @allure.feature('Регистрация по email')
    @allure.label('owner', 'irauchuvatova')
    @allure.label('layer', 'API')
    @allure.tag('smoke', 'regress', 'API', 'registration')
    @allure.severity('critical')
    def test_post_register_user_short_password(self, endpoint=endpoint):
        schema = load_schema(UNSUCCESSFUL_REGISTER_USER_PATH)
        with allure.step('Создать пользователя с паролем меньше 5 символов'):
            new_user = new_user_with_short_password_for_api()

        with allure.step(f'Отправить POST-запрос на {endpoint} для регистрации нового пользователя'):
            result: Response = requests.post(url=API_URL + endpoint, json=new_user)

        with allure.step('Проверить, что API возвращает 422 код ответа'):
            assert result.status_code == 422
        with allure.step('Провалидировать схему ответа'):
            jsonschema.validate(result.json(), schema)
        with allure.step('Проверить сообщение о минимально допустимых 5 символах в пароле'):
            assert 'ensure this value has at least 5 characters' in result.text

        allure.attach(body=result.request.url,
                      name="Request url",
                      attachment_type=AttachmentType.TEXT)
        allure.attach(body=result.request.method,
                      name="Request method",
                      attachment_type=AttachmentType.TEXT)
        allure.attach(body=result.request.body,
                      name="Request body",
                      attachment_type=AttachmentType.JSON,
                      extension="json")
        allure.attach(body=json.dumps(result.json(), indent=4, ensure_ascii=True),
                      name="Response body",
                      attachment_type=AttachmentType.JSON,
                      extension="json")
        logging.info(result.request.url)
        logging.info(result.status_code)
        logging.info(result.text)
