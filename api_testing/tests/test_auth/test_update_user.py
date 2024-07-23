import allure
import requests

from api_testing.data import Urls
from api_testing.tests.test_auth.test_create_user import TestCreateUser


class TestUpdateUser:

    @allure.title('Обновление данных пользователей с авторизацией')
    def test_update_user_with_authorization_positive_result(self, return_data_pass):
        email = return_data_pass['email']
        name = return_data_pass['name']
        payload = {
            "email": f'123{email}',
            "name": f'Mk{name}'
        }
        print(return_data_pass)
        print(payload)
        response = requests.patch(f'{Urls.URL}{Urls.UPDATE_USER}',
                                 data=payload, headers={'Authorization': return_data_pass['accessToken']})
        r = response.json()
        print(r)
        assert response.status_code == 200
        assert payload['email'] == r['user']['email']
        assert payload['name'] == r['user']['name']

    @allure.title('Обновление email пользователя без авторизации')
    def test_update_user_without_authorization_negative_result(self, return_data_pass):
        email = return_data_pass['email']
        name = return_data_pass['name']
        payload = {
            "email": f'123{email}',
            "name": name
        }
        print(return_data_pass)
        print(payload)
        response = requests.patch(f'{Urls.URL}{Urls.UPDATE_USER}',
                                  data=payload)
        r = response.json()
        print(r)
        assert response.status_code == 401
        assert response.text == '{"success":false,"message":"You should be authorised"}'

    @allure.title('Обновление имени пользователя без авторизации')
    def test_update_user_without_authorization_negative_result(self, return_data_pass):
        email = return_data_pass['email']
        name = return_data_pass['name']
        payload = {
            "email": email,
            "name": f'Mk{name}'
        }
        print(return_data_pass)
        print(payload)
        response = requests.patch(f'{Urls.URL}{Urls.UPDATE_USER}',
                                  data=payload)
        r = response.json()
        print(r)
        assert response.status_code == 401
        assert response.text == '{"success":false,"message":"You should be authorised"}'

    @allure.title('Обновление email на уже существующий email')
    def test_update_user_with_authorization_positive_result\
                    (self, return_data_pass, register_new_user_2):
        user_2 = TestCreateUser()
        user_2.test_create_auth_new_user_positive_result(register_new_user_2)
        email_2 = register_new_user_2['email']
        payload = {
            "email": email_2
        }
        response = requests.patch(f'{Urls.URL}{Urls.UPDATE_USER}',
                                  data=payload, headers={'Authorization': return_data_pass['accessToken']})
        print(response.status_code)
        print(response.text)
        assert response.status_code == 403
        assert response.text == '{"success":false,"message":"User with such email already exists"}'
