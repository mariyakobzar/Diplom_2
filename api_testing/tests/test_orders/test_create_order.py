import json

import allure
import pytest
import requests

from api_testing.data import Urls
from api_testing.tests.test_auth.test_create_user import TestCreateUser


class TestCreateOrder:

    @pytest.mark.parametrize(
        'payload',
        [
            {"ingredients": [Urls.BUNS["bun_1"], Urls.MAIN["main_1"], Urls.SAUCE["sauce_1"]]},
            {"ingredients": [Urls.BUNS["bun_1"], Urls.BUNS["bun_2"], Urls.MAIN["main_1"], Urls.MAIN["main_2"],
                                                   Urls.MAIN["main_3"], Urls.MAIN["main_4"], Urls.MAIN["main_5"],
                                                   Urls.MAIN["main_6"], Urls.MAIN["main_7"], Urls.MAIN["main_8"],
                                                   Urls.MAIN["main_9"], Urls.SAUCE["sauce_1"], Urls.SAUCE["sauce_2"],
                                                   Urls.SAUCE["sauce_3"], Urls.SAUCE["sauce_4"]]},
            {"ingredients": [Urls.BUNS["bun_1"], Urls.MAIN["main_1"]]},
            {"ingredients": [Urls.BUNS["bun_1"], Urls.SAUCE["sauce_1"]]},
            {"ingredients": [Urls.MAIN["main_1"], Urls.SAUCE["sauce_1"]]}
        ]
    )
    @allure.title('Создание заказа без авторизации')
    def test_create_order_without_auth_positive_result(self, payload):
        #t = json.dumps(payload)
        response = requests.post(f'{Urls.URL}{Urls.CREATE_ORDER}',
                                 data=payload)#, headers={'Authorization': return_data_pass['accessToken']})
        r = response.json()
        print(r)
        print(r['order']['number'])

        assert response.status_code == 200
        assert r['success'] == True
        if Urls.BUNS["bun_1"] == "61c0c5a71d1f82001bdaaa6d":
            assert 'бургер' in r['name']
        else:
            assert 'бургер' in r['name']


    @allure.title('Создание заказа с авторизацией')
    def test_create_order_with_auth_positive_result(self, return_data_pass):
        payload = {"ingredients": [Urls.BUNS["bun_1"], Urls.MAIN["main_1"], Urls.SAUCE["sauce_1"]]}
        print(payload)
        json_payload = json.dumps(payload)
        print(type(payload))
        print(type(json_payload))
        response = requests.post(f'{Urls.URL}{Urls.CREATE_ORDER}',
                                 data=payload, headers={'Authorization': return_data_pass['accessToken']})
        r = response.json()

        assert response.status_code == 200
        assert r['success'] == True
        if Urls.BUNS["bun_1"] == "61c0c5a71d1f82001bdaaa6d":
            assert 'бессмертный флюоресцентный бургер' in r['name']
        else:
            assert 'бессмертный краторный бургер' in r['name']


    @allure.title('Создание заказа с неверным хешем ингредиентов')
    def test_create_order_with_wrong_ingr_negative_result(self):

        payload = {"ingredients": [f'1{Urls.BUNS["bun_1"]}', f'1{Urls.MAIN["main_1"]}', f'{Urls.SAUCE["sauce_1"]}']}
        response = requests.post(f'{Urls.URL}{Urls.CREATE_ORDER}',
                                 data=payload)

        assert response.status_code == 500


