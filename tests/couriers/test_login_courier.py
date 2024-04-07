import allure

from helper_functions.courier_helpers import CourierHelpers
from helper_functions.login_courier import LoginCourier
from helper_functions.shared_helper_funcs import HelperFuncs


class TestLoginCourier():

    @allure.title('Авторизация  существующего курьера, по логину и паролю успешна')
    def test_login_courier_with_all_required_params_success(self, courier_login_valid_creds):
        login_courier = LoginCourier()
        response = login_courier.login_courier(courier_login_valid_creds[0])
        assert response.status_code == 200
        assert response.reason == 'OK'
        assert 'id' in response.json()
        assert type(response.json()['id']) == int

    @allure.title('Авторизация существующего курьера. Если не передан логин или пароль, не успешна')
    def test_login_courier_with_empty_login_or_password_fail_1(self, courier_login_valid_login_and_password):
        login_courier = LoginCourier()
        response = login_courier.login_courier({
            'login': courier_login_valid_login_and_password.get('login'),
            'password': courier_login_valid_login_and_password.get('password'),
        })
        assert response.status_code == 400
        assert response.reason == 'Bad Request'
        assert response.json()['code'] == 400
        assert response.json()['message'] == "Недостаточно данных для входа"

    @allure.title('Авторизация существующего курьера. Если неправильный логин или пароль, не успешна')
    def test_login_courier_with_wrong_login_or_password_fail_1(self, courier_login_valid_login_and_password):
        login_courier = LoginCourier()
        login = courier_login_valid_login_and_password.get('login')
        login = login if bool(login) else HelperFuncs.generate_random_string(8)
        password = courier_login_valid_login_and_password.get('password')
        password = password if bool(password) else HelperFuncs.generate_random_string(8)
        response = login_courier.login_courier({
            'login': login,
            'password': password,
        })
        assert response.status_code == 404
        assert response.reason == 'Not Found'
        assert response.json()['message'] == "Учетная запись не найдена"

    @allure.title('Авторизация НЕ существующего курьера не успешна')
    def test_login_courier_with_not_existing_courier(self, courier_login_valid_creds):
        courier_helpers = CourierHelpers()
        courier_helpers.delete_couriers_by_id(courier_login_valid_creds[1])
        login_courier = LoginCourier()
        response = login_courier.login_courier(courier_login_valid_creds[0])
        assert response.status_code == 404
        assert response.reason == 'Not Found'
        assert response.json()['message'] == "Учетная запись не найдена"
