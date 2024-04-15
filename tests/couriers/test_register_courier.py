import allure
import pytest

from helper_functions.register_courier import RegisterCourier
from constants.response_error_messages import ResponseErrorMessages


class TestRegisterCourier:

    @allure.title('Регистрация курьера. Если переданы валидные логин, пароль и имя, успешна')
    def test_register_courier_with_all_fields_filled_success(self):
        register_courier = RegisterCourier()
        payload = register_courier.get_register_payload()
        response = register_courier.register_new_courier_request(payload)
        assert response.status_code == 201
        assert response.reason == 'Created'
        assert response.json()['ok'] == True

    @allure.title('Регистрация курьера. Если переданы данные существующего курьера, не успешна')
    def test_register_courier_with_registered_data_fail(self):
        register_courier = RegisterCourier()
        payload = register_courier.get_register_payload()
        register_courier.register_new_courier_request(payload)
        response = register_courier.register_new_courier_request(payload)
        assert response.status_code == 409
        assert response.reason == 'Conflict'
        assert response.json()['message'] == ResponseErrorMessages.LOGIN_ALREADY_IN_USE_TRY_ANOTHER_ONE

    @allure.title('Регистрация курьера. Если не передан логин или пароль, не успешна')
    @pytest.mark.parametrize(
        'entity',
        ['login', 'password']
    )
    def test_register_courier_with_empty_required_entity_fail(self, entity):
        register_courier = RegisterCourier()
        payload = register_courier.get_register_payload()
        del payload[entity]
        response = register_courier.register_new_courier_request(payload)
        assert response.status_code == 400
        assert response.reason == 'Bad Request'
        assert response.json()['message'] == ResponseErrorMessages.NOT_ENOUGH_DATA_TO_REGISTER
        assert response.json()['code'] == 400

    @allure.title('Регистрация существующего курьера. Если не передано имя, успешна')
    def test_register_courier_with_empty_name_success(self):
        register_courier = RegisterCourier()
        payload = register_courier.get_register_payload()
        del payload['firstName']
        response = register_courier.register_new_courier_request(payload)
        assert response.status_code == 201
        assert response.reason == 'Created'
        assert response.json()['ok'] == True

    @allure.title('Регистрация курьера. Если передан логин существующего курьера, не успешна')
    def test_register_courier_with_registered_login_fail(self):
        register_courier = RegisterCourier()
        payload = register_courier.get_register_payload()
        login = payload['login']
        register_courier.register_new_courier_request(payload)
        registered_login_payload = {
            **register_courier.get_register_payload(),
            'login': login
        }
        response = register_courier.register_new_courier_request(registered_login_payload)
        assert response.status_code == 409
        assert response.reason == 'Conflict'
        assert response.json()['message'] == ResponseErrorMessages.LOGIN_ALREADY_IN_USE_TRY_ANOTHER_ONE
