from helper_functions.delete_courier import DeleteCourier
from helper_functions.login_courier import LoginCourier


class TestDeleteCourier:

    def test_delete_courier_with_existing_id_success(self, courier_login_valid_creds):
        login_courier = LoginCourier()
        courier_id = courier_login_valid_creds[1]
        delete_courier = DeleteCourier()
        response = delete_courier.delete_couriers_by_id(courier_id)
        assert response.status_code == 200
        assert response.reason == 'OK'
        assert response.json()['ok'] == True

    def test_delete_courier_without_id_fail(self):
        delete_courier = DeleteCourier()
        response = delete_courier.delete_couriers_by_id('')
        assert response.status_code == 400
        assert response.reason == 'Bad Request'
        assert response.json()['message'] == "Недостаточно данных для удаления курьера"

    def test_delete_courier_with_not_existing_courier_id_fail(self, courier_login_valid_creds):
        login_courier = LoginCourier()
        courier_id = courier_login_valid_creds[1]
        delete_courier = DeleteCourier()
        delete_courier.delete_couriers_by_id(courier_id)
        response = delete_courier.delete_couriers_by_id(courier_id)
        assert response.status_code == 404
        assert response.reason == 'Not Found'
        assert "Курьера с таким id нет" in response.json()['message']
