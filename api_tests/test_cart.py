import logging

import allure
import jsonschema
import requests
from allure_commons.types import AttachmentType
from requests import Response

from conftest import *
from schemas.load_schema import *


@allure.epic('API корзины покупок')
@allure.story('Просмотр корзины')
class TestCart:
    endpoint = '/cart/status'

    @allure.title('Просмотр пустой корзины неавторизованного пользователя')
    @allure.feature('Неавторизованный пользователь')
    @allure.label('owner', 'irauchuvatova')
    @allure.tag('smoke', 'regress', 'API', 'cart')
    @allure.severity('critical')
    def test_get_status_empty_cart(self, endpoint=endpoint):
        schema = load_schema(STATUS_CART_PATH)

        with allure.step(f'Отправить GET-запрос на {endpoint} для просмотра корзины'):
            result: Response = requests.get(url=API_URL + endpoint)

        with allure.step('Проверить, что API возвращает 200 код ответа'):
            assert result.status_code == 200
        with allure.step('Проверить, что в корзине пусто'):
            assert result.json().get('payload').get("data").get('count') == 0
        with allure.step('Провалидировать схему ответа'):
            jsonschema.validate(result.json(), schema)

        allure.attach(body=result.request.url,
                      name="Request url",
                      attachment_type=AttachmentType.TEXT)
        allure.attach(body=result.request.method,
                      name="Request method",
                      attachment_type=AttachmentType.TEXT)
        allure.attach(body=json.dumps(result.request.body, indent=4, ensure_ascii=True),
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
