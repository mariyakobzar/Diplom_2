import allure
import requests

from api_testing.data import Urls, Responses


class TestCreateUser:

    @allure.title('Создание пользователя')
    def test_create_auth_new_user_positive_result(self, user_credentials):
        payload = user_credentials
        response = requests.post(f'{Urls.URL}{Urls.CREATE_USER}', data=payload)
        r = response.json()

        assert response.status_code == 200
        assert r['success'] == True

    @allure.title('Создание уже зарегистрированного пользователя')
    def test_create_auth_the_same_user_negative_result(self, return_data_pass):
        payload = return_data_pass
        response = requests.post(f'{Urls.URL}{Urls.CREATE_USER}', data=payload)

        assert response.status_code == 403
        assert response.text == Responses.USER_ALREADY_EXISTS

    @allure.title('Создание пользователя без email')
    def test_create_auth_without_email_negative_result(self, user_credentials):
        payload = {
            "password": user_credentials['password'],
            "name": user_credentials['name']
        }
        response = requests.post(f'{Urls.URL}{Urls.CREATE_USER}', data=payload)
        assert response.status_code == 403
        assert response.text == Responses.EMAIL_PASS_NAME_REQUIRED

    @allure.title('Создание пользователя без password')
    def test_create_auth_without_password_negative_result(self, user_credentials):
        payload = {
            "email": user_credentials['email'],
            "name": user_credentials['name']
        }
        response = requests.post(f'{Urls.URL}{Urls.CREATE_USER}', data=payload)
        assert response.status_code == 403
        assert response.text == Responses.EMAIL_PASS_NAME_REQUIRED

    @allure.title('Создание пользователя без name')
    def test_create_auth_without_email_negative_result(self, user_credentials):
        payload = {
            "email": user_credentials['email'],
            "password": user_credentials['password']
        }
        response = requests.post(f'{Urls.URL}{Urls.CREATE_USER}', data=payload)
        assert response.status_code == 403
        assert response.text == Responses.EMAIL_PASS_NAME_REQUIRED
