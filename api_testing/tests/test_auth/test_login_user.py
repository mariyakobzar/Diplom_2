import allure
import requests

from api_testing.data import Urls, Responses


class TestLoginUser:

    @allure.title('Логин пользователя')
    def test_login_user_positive_result(self, return_data_pass):
        payload = {
            "email": return_data_pass['email'],
            "password": return_data_pass['password']
        }
        response = requests.post(f'{Urls.URL}{Urls.LOGIN_USER}',
                                 data=payload)
        r = response.json()
        assert response.status_code == 200
        assert r['success'] == True

    @allure.title('Логин пользователя с неверным email')
    def test_login_user_negative_result(self, return_data_pass):
        email = return_data_pass['email']
        payload = {
            "email": f'123{email}',
            "password": return_data_pass['password']
        }
        response = requests.post(f'{Urls.URL}{Urls.LOGIN_USER}',
                                 data=payload)

        assert response.status_code == 401
        assert response.text == Responses.EMAIL_PASS_INCORRECT

    @allure.title('Логин пользователя с неверным паролем')
    def test_login_user_negative_result(self, return_data_pass):
        password = return_data_pass['password']
        payload = {
            "email": return_data_pass['email'],
            "password": f'123{password}'
        }
        response = requests.post(f'{Urls.URL}{Urls.LOGIN_USER}',
                                 data=payload)

        assert response.status_code == 401
        assert response.text == Responses.EMAIL_PASS_INCORRECT
