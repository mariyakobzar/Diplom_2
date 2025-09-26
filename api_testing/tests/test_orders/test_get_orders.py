
import allure
import requests

from api_testing.data import Urls, Responses
from api_testing.tests.test_orders.test_create_order import TestCreateOrder


class TestGetOrders:

    @allure.title('Получение всех заказов с авторизацией')
    def test_get_all_orders_positive_result(self, return_data_pass):
        user = TestCreateOrder()
        user.test_create_order_with_auth_positive_result(return_data_pass)

        response = requests.get(f'{Urls.URL}{Urls.GET_ORDERS}',
                                headers={'Authorization': return_data_pass['accessToken']})
        r = response.json()
        id = r['orders'][0]['_id']
        assert r['orders'][0]['_id'] == id
        assert response.status_code == 200
        assert r['success'] == True

    @allure.title('Получение всех заказов без атворизации')
    def test_get_user_orders_positive_result(self, return_data_pass):
        user = TestCreateOrder()
        user.test_create_order_with_auth_positive_result(return_data_pass)

        response = requests.get(f'{Urls.URL}{Urls.GET_ORDERS}')
        r = response.json()
        id = r['orders'][0]['_id']
        assert r['orders'][0]['_id'] == id
        assert response.status_code == 200
        assert r['success'] == True

    @allure.title('Получить все заказы конкретного пользователя, с авторизацией')
    def test_get_user_orders_positive_result(self, return_data_pass):
        user = TestCreateOrder()
        user.test_create_order_with_auth_positive_result(return_data_pass)

        response = requests.get(f'{Urls.URL}{Urls.GET_ORDERS_USER}',
                                headers={'Authorization': return_data_pass['accessToken']})
        r = response.json()
        id = r['orders'][0]['_id']
        assert r['orders'][0]['_id'] == id
        assert response.status_code == 200
        assert r['success'] == True

    @allure.title('Получить все заказы конкретного пользователя, без авторизации')
    def test_get_user_orders_negative_result(self, return_data_pass):
        user = TestCreateOrder()
        user.test_create_order_with_auth_positive_result(return_data_pass)

        response = requests.get(f'{Urls.URL}{Urls.GET_ORDERS_USER}')
        assert response.status_code == 401
        assert response.text == Responses.NO_AUTHORISATION
