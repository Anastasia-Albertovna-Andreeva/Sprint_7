import requests
import allure
import pytest
from data import Data
from urls import Urls
from helpers import create_random_login, create_random_password, create_random_firstname


class TestCourierCreate:

    @allure.title('Проверка успешного курьера с валидными данными')
    @allure.description('Проверка кода и тела ответа при успешном создании курьера')
    def test_create_courier_account_success(self):
        payload = {
            'login': create_random_login(),
            'password': create_random_password(),
            'firstName': create_random_firstname()
        }
        response = requests.post(Urls.URL_courier_create, data=payload)
        assert response.status_code == 201
        assert response.json().get('ok') is True

    @allure.title('Проверка ошибки при повторном создании курьера с уже используемым логином')
    @allure.description('Проверяются код и тело ответа.')
    def test_create_courier_account_login_taken_conflict(self):
        payload = {
            'login': Data.valid_login,
            'password': create_random_password(),
            'firstName': create_random_firstname()
        }
        response = requests.post(Urls.URL_courier_create, data=payload)
        assert response.status_code == 409
        # Проверяем только поле message
        assert response.json().get('message') == 'Этот логин уже используется. Попробуйте другой.'

    @allure.title('Проверка получения ошибки при создании курьера с незаполненными обязательными полями')
    @allure.description('В тест по очереди передаются наборы данных с пустым логином или паролем. '
                        'Проверяются код и тело ответа.')
    @pytest.mark.parametrize('empty_credentials', [
        {'login': '', 'password': create_random_password(), 'firstName': create_random_firstname()},
        {'login': create_random_login(), 'password': '', 'firstName': create_random_firstname()}
    ])
    def test_create_courier_account_with_empty_required_fields(self, empty_credentials):
        response = requests.post(Urls.URL_courier_create, data=empty_credentials)
        assert response.status_code == 400
        # Проверяем только поле message
        assert response.json().get('message') == 'Недостаточно данных для создания учетной записи'
