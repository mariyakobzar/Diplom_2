import pytest
import requests

from api_testing.data import Urls
from api_testing.helpers import Helpers


@pytest.fixture()
def user_credentials():

    # генерируем email, password, name
    def generate_payload():
        email = Helpers.generate_random_string(5)
        password = Helpers.generate_random_string(10)
        name = Helpers.generate_random_string(10)

        # собираем тело запроса
        return {
            "email": f'{email}@gmail.com',
            "password": password,
            "name": name
        }
    return generate_payload()

@pytest.fixture()
def return_data_pass(user_credentials):

    user = user_credentials

    # отправляем запрос на регистрацию пользователя и сохраняем ответ в переменную response
    response = requests.post(f'{Urls.URL}{Urls.CREATE_USER}', data=user)
    r = response.json()

    # создаём словарь, чтобы метод мог его вернуть
    data_pass = {}

    # если регистрация прошла успешно, добавляем в список email, password, name, accessToken пользователя
    data_pass['email'] = user['email']
    data_pass['password'] = user['password']
    data_pass['name'] = user['name']
    data_pass['accessToken'] = r['accessToken']
    yield data_pass
    response = requests.delete(f'{Urls.URL}{Urls.DELETE_USER}', headers={'Authorization': data_pass['accessToken']})



@pytest.fixture()
def user2_credentials():

    # генерируем email, password и name пользователя
    def generate_payload():
        email = Helpers.generate_random_string(5)
        password = Helpers.generate_random_string(10)
        name = Helpers.generate_random_string(10)

        # собираем тело запроса
        return {
            "email": f'{email}@gmail.com',
            "password": password,
            "name": name
        }
    return generate_payload()


@pytest.fixture()
def return_data_pass_user2(user2_credentials):

    user = user2_credentials

    # отправляем запрос на регистрацию пользователя и сохраняем ответ в переменную response
    response = requests.post(f'{Urls.URL}{Urls.CREATE_USER}', data=user)
    r = response.json()

    # создаём словарь, чтобы метод мог его вернуть
    data_pass = {}

    # если регистрация прошла успешно, добавляем в список email, password, name, accessToken пользователя
    data_pass['email'] = user['email']
    data_pass['password'] = user['password']
    data_pass['name'] = user['name']
    data_pass['accessToken'] = r['accessToken']
    yield data_pass
    response = requests.delete(f'{Urls.URL}{Urls.DELETE_USER}', headers={'Authorization': data_pass['accessToken']})


