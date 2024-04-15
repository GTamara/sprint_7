import allure

from helper_functions.courier_helpers import CourierHelpers
from helper_functions.login_courier import LoginCourier
from constants.response_error_messages import ResponseErrorMessages


class TestDeleteCourier:

    @allure.title('Удаление существующего курьера по id успешно')
    def test_delete_courier_with_existing_id_success(self, courier_login_valid_creds):
        courier_id = courier_login_valid_creds[1]
        courier_helpers = CourierHelpers()
        response = courier_helpers.delete_couriers_by_id(courier_id)
        assert response.status_code == 200
        assert response.reason == 'OK'
        assert response.json()['ok'] == True

    @allure.title('Удаление курьера, если id не передано, не успешно')
    def test_delete_courier_without_id_fail(self):
        courier_helpers = CourierHelpers()
        response = courier_helpers.delete_couriers_by_id('')
        assert response.status_code == 400
        assert response.reason == 'Bad Request'
        assert response.json()['message'] == ResponseErrorMessages.NOT_ENOUGH_DATA_FOR_COURIER_DELETING

    @allure.title('Удаление курьера, по id не существующего курьера, не успешно')
    def test_delete_courier_with_not_existing_courier_id_fail(self, courier_login_valid_creds):
        courier_id = courier_login_valid_creds[1]
        courier_helpers = CourierHelpers()
        courier_helpers.delete_couriers_by_id(courier_id)
        response = courier_helpers.delete_couriers_by_id(courier_id)
        assert response.status_code == 404
        assert response.reason == 'Not Found'
        assert ResponseErrorMessages.COURIER_ID_NOT_EXISTS in response.json()['message']
