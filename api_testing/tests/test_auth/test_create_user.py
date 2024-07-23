import allure
import requests

from api_testing.data import Urls


class TestCreateUser:

    @allure.title('Создание пользователя')
    def test_create_auth_new_user_positive_result(self, register_new_user):
        payload = register_new_user
        print(payload)
        response = requests.post(f'{Urls.URL}{Urls.CREATE_USER}', data=payload)
        r = response.json()
        print(r)

        assert response.status_code == 200
        assert r['success'] == True

    @allure.title('Создание уже зарегистрированного пользователя')
    def test_create_auth_the_same_user_negative_result(self, register_new_user):
        self.test_create_auth_new_user_positive_result(register_new_user)
        payload = register_new_user
        response = requests.post(f'{Urls.URL}{Urls.CREATE_USER}', data=payload)
        r = response.json()
        print(r)

        assert response.status_code == 403
        assert response.text == '{"success":false,"message":"User already exists"}'

    @allure.title('Создание пользователя без email')
    def test_create_auth_without_email_negative_result(self, register_new_user):
        param = register_new_user
        print(param)
        payload = {
            "password": param['password'],
            "name": param['name']
        }
        response = requests.post(f'{Urls.URL}{Urls.CREATE_USER}', data=payload)
        r = response.json()
        print(r)
        assert response.status_code == 403
        assert response.text == '{"success":false,"message":"Email, password and name are required fields"}'

    @allure.title('Создание пользователя без password')
    def test_create_auth_without_password_negative_result(self, register_new_user):
        param = register_new_user
        print(param)
        payload = {
            "email": param['email'],
            "name": param['name']
        }
        response = requests.post(f'{Urls.URL}{Urls.CREATE_USER}', data=payload)
        r = response.json()
        print(r)
        assert response.status_code == 403
        assert response.text == '{"success":false,"message":"Email, password and name are required fields"}'

    @allure.title('Создание пользователя без name')
    def test_create_auth_without_email_negative_result(self, register_new_user):
        param = register_new_user
        print(param)
        payload = {
            "email": param['email'],
            "password": param['password']
        }
        response = requests.post(f'{Urls.URL}{Urls.CREATE_USER}', data=payload)
        r = response.json()
        print(r)
        assert response.status_code == 403
        assert response.text == '{"success":false,"message":"Email, password and name are required fields"}'
