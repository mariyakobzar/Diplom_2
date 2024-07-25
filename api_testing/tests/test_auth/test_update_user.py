import allure
import requests

from api_testing.data import Urls, Responses
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
        response = requests.patch(f'{Urls.URL}{Urls.UPDATE_USER}',
                                 data=payload, headers={'Authorization': return_data_pass['accessToken']})
        r = response.json()
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
        response = requests.patch(f'{Urls.URL}{Urls.UPDATE_USER}',
                                  data=payload)
        assert response.status_code == 401
        assert response.text == Responses.NO_AUTHORISATION

    @allure.title('Обновление имени пользователя без авторизации')
    def test_update_user_without_authorization_negative_result(self, return_data_pass):
        email = return_data_pass['email']
        name = return_data_pass['name']
        payload = {
            "email": email,
            "name": f'Mk{name}'
        }
        response = requests.patch(f'{Urls.URL}{Urls.UPDATE_USER}',
                                  data=payload)
        assert response.status_code == 401
        assert response.text == Responses.NO_AUTHORISATION

    @allure.title('Обновление email на уже существующий email')
    def test_update_user_with_authorization_positive_result\
                    (self, return_data_pass, return_data_pass_user2):
        email_2 = return_data_pass_user2['email']
        payload = {
            "email": email_2
        }
        response = requests.patch(f'{Urls.URL}{Urls.UPDATE_USER}',
                                  data=payload, headers={'Authorization': return_data_pass['accessToken']})
        assert response.status_code == 403
        assert response.text == Responses.USER_WITH_SUCH_EMAIL_ALREADY_EXISTS
