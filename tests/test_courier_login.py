import requests
import allure
import pytest
from data import Data
from urls import Urls
from helpers import create_random_login, create_random_password


class TestCourierLogin:

    @allure.title('Проверка успешной авторизации курьера при вводе валидных данных')
    @allure.description('Проверка кода и тела ответа при успешной авторизации курьера')
    def test_courier_login_success(self):
        response = requests.post(Urls.URL_courier_login, data=Data.valid_courier_data)
        assert response.status_code == 200
        # Проверяем наличие id в ответе
        assert 'id' in response.json()

    @allure.title('Проверка получения ошибки при авторизации курьера с невалидными данными')
    @allure.description('При тестировании передаются наборы данных с невалидным логином и паролем, проверяется код и тело ответа.')
    @pytest.mark.parametrize('nonexistent_credentials', [
        {'login': create_random_login(), 'password': create_random_password()},
        Data.courier_data_with_wrong_password
    ])
    def test_courier_login_nonexistent_data_not_found(self, nonexistent_credentials):
        response = requests.post(Urls.URL_courier_login, data=nonexistent_credentials)
        assert response.status_code == 404
        # Проверяем только поле message
        assert response.json().get('message') == 'Учетная запись не найдена'

    @allure.title('Проверка получения ошибки при авторизации курьера с пустым логином или паролем')
    @allure.description('При тестировании передаются наборы данных с пустым логином или паролем. Проверяются код и тело ответа.')
    @pytest.mark.parametrize('empty_credentials', [
        {'login': '', 'password': create_random_password()},
        {'login': Data.valid_login, 'password': ''}
    ])
    def test_courier_login_empty_credentials_bad_request(self, empty_credentials):
        response = requests.post(Urls.URL_courier_login, data=empty_credentials)
        assert response.status_code == 400
        # Проверяем только поле message
        assert response.json().get('message') == 'Недостаточно данных для входа'
