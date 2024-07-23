import pytest
import requests
import random
import string

from api_testing.data import Urls

@pytest.fixture()
def register_new_user():
    # метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    # генерируем email, password, name
    def generate_payload():
        email = generate_random_string(5)
        password = generate_random_string(10)
        name = generate_random_string(10)

        # собираем тело запроса
        return {
            "email": f'{email}@gmail.com',
            "password": password,
            "name": name
        }
    return generate_payload()

@pytest.fixture()
def return_data_pass(register_new_user):

    user = register_new_user

    # отправляем запрос на регистрацию пользователя и сохраняем ответ в переменную response
    response = requests.post('https://stellarburgers.nomoreparties.site/api/auth/register', data=user)
    r = response.json()

    # создаём словарь, чтобы метод мог его вернуть
    data_pass = {}

    # если регистрация прошла успешно, добавляем в список email, password, name, accessToken пользователя
    def registration(data):
        data_pass['email'] = data['email']
        data_pass['password'] = data['password']
        data_pass['name'] = data['name']
        data_pass['accessToken'] = r['accessToken']

    registration(user)
    # возвращаем словарь
    yield data_pass
    response = requests.delete(f'{Urls.URL}{Urls.DELETE_USER}', headers={'Authorization': data_pass['accessToken']})



@pytest.fixture()
def register_new_user_2():
    # метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    # генерируем email, password и name пользователя
    def generate_payload():
        email = generate_random_string(5)
        password = generate_random_string(10)
        name = generate_random_string(10)

        # собираем тело запроса
        return {
            "email": f'{email}@gmail.com',
            "password": password,
            "name": name
        }
    return generate_payload()


