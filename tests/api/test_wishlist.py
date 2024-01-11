import json
import logging

import allure
import requests
from allure_commons.types import AttachmentType
from requests import Response

from tests.ui.conftest import API_RECOMMENDED, API_URL


@allure.epic('API Отложенных книг')
@allure.story('Добавление и удаление из Отложенных неавторизованным пользователем')
class TestWishlist:
    endpoint = '/wishlist/arts/'

    @allure.title('Добавление неавторизованным пользователем книги в Отложенные')
    @allure.feature('Неавторизованный пользователь')
    @allure.label('owner', 'irauchuvatova')
    @allure.label('layer', 'API')
    @allure.tag('smoke', 'regress', 'API', 'wishlist')
    @allure.severity('critical')
    def test_put_add_to_wishlist(self, endpoint=endpoint):
        with allure.step('Получить id книги  из раздела Рекомендации для вас'):
            book_list: Response = requests.get(url=API_RECOMMENDED)
            book_id = book_list.json().get('payload').get("data")[0].get('id')

        with allure.step(f'Отправить PUT-запрос на {endpoint} для добавления книги в Отложенные'):
            result: Response = requests.put(url=API_URL + endpoint + f'{book_id}')

        with allure.step('Проверить, что API возвращает 204 код ответа'):
            assert result.status_code == 204
        with allure.step('Проверить, что в ответе приходит cookie LKS со значением отложенной книги'):
            assert result.cookies.get('LKS') == f'{book_id}'
        with allure.step('Проверить, что не приходит body в ответе'):
            assert not result.content

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
        allure.attach(body=str(result.cookies),
                      name="Response cookies",
                      attachment_type=AttachmentType.TEXT,
                      extension="txt")
        logging.info(result.request.url)
        logging.info(result.status_code)
        logging.info(result.cookies)
        logging.info(result.text)

    @allure.title('Удаление неавторизованным пользователем книги из Отложенные')
    @allure.feature('Неавторизованный пользователь')
    @allure.label('owner', 'irauchuvatova')
    @allure.label('layer', 'API')
    @allure.tag('smoke', 'regress', 'API', 'wishlist')
    @allure.severity('critical')
    def test_delete_from_wishlist(self, endpoint=endpoint):
        with allure.step('Получить id книги из раздела Рекомендации для вас'):
            book_list: Response = requests.get(url=API_RECOMMENDED)
            book_id = book_list.json().get('payload').get("data")[0].get('id')
        with allure.step('Добавить книгу в Отложенные'):
            added_to_wishlist: Response = requests.put(url=API_URL + endpoint + f'{book_id}')

        with allure.step(f'Отправить DELETE-запрос на {endpoint} для удаления добавленной книги из Отложенных'):
            result: Response = requests.delete(url=API_URL + endpoint + f'{book_id}', headers={'Wishlist': f'{book_id}'})

        with allure.step('Проверить, что API возвращает 204 код ответа'):
            assert result.status_code == 204
        with allure.step('Проверить, что в ответе не приходит cookie LKS'):
            assert not result.cookies.get('LKS')
        with allure.step('Проверить, что не приходит body в ответе'):
            assert not result.content

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
        allure.attach(body=str(result.cookies),
                      name="Response cookies",
                      attachment_type=AttachmentType.TEXT,
                      extension="txt")
        logging.info(result.request.url)
        logging.info(result.status_code)
        logging.info(result.cookies)
        logging.info(result.text)
