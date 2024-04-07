import pytest

from helper_functions.login_courier import LoginCourier
from helper_functions.register_courier import RegisterCourier



class TestLoginCourier():

    # invalid_login_credentials = []
    # login_creds = {}
    # @classmethod
    # def setup_class(cls):
    #     print('!!!!!!!!!!!!!!setup_class')
    #     register_courier = RegisterCourier()
    #     register_courier.register_new_courier()
    #     cls.login_creds = register_courier.register_new_courier()
    #     login_courier = LoginCourier()
    # cls.invalid_login_credentials = courier_login_empty_login_or_password_creds
    # login_courier.get_invalid_login_or_password_payload_list(
    #     cls.login_creds['login'],
    #     cls.login_creds['password'],
    # )

    # def test_login_courier_with_all_required_params_success(self):
    #     login_courier = LoginCourier()
    #     response = login_courier.login_courier(self.login_creds)
    #     # print(courier_login_credentials)
    #     assert response.status_code == 200
    #     assert response.reason == 'OK'
    #     assert 'id' in response.json()

    def test_login_courier_with_all_required_params_success(self, courier_login_valid_creds):
        login_courier = LoginCourier()
        response = login_courier.login_courier(courier_login_valid_creds[0])
        # print(courier_login_credentials)
        assert response.status_code == 200
        assert response.reason == 'OK'
        assert 'id' in response.json()

    def login_courier_with_empty_login_or_password_fail(self, payload):
        # def test_login_courier_with_empty_login_or_password_fail(self, courier_login_credentials):
        login_courier = LoginCourier()
        #     del courier_login_credentials['login']
        response = login_courier.login_courier(payload)
        # print(courier_login_credentials)
        assert response.status_code == 400
        assert response.reason == 'Bad Request'
        assert response.json()['code'] == 400
        assert response.json()['message'] == "Недостаточно данных для входа"

    def test_login_courier_with_empty_login_fail(self, courier_login_valid_creds):
        self.login_courier_with_empty_login_or_password_fail({
            'login': courier_login_valid_creds['login']
        })

    def test_login_courier_with_empty_password_fail(self, courier_login_valid_creds):
        self.login_courier_with_empty_login_or_password_fail({
            'password': courier_login_valid_creds['password']
        })

        # @pytest.mark.parametrize('payload',
        #                          [('courier_login_empty_login_or_password_creds')]
        #                          )
        # def test_login_courier_with_empty_login_or_password_fail(
        #         payload,
        #         courier_login_empty_login_or_password_creds,
        #         request
        # ):
        #     my_fixture = request.getfixturevalue(courier_login_empty_login_or_password_creds)
        #     print('!!!!!!!!!!!!my_fixture', my_fixture)
        #     login_courier = LoginCourier()
        #     response = login_courier.login_courier(payload)
        #     assert response.status_code == 400
        #     assert response.reason == 'Bad Request'
        #     assert response.json()['code'] == 400
        #     assert response.json()['message'] == "Недостаточно данных для входа"


        # @pytest.mark.parametrize('payload',
        #                          [pytest.lazy_fixture('courier_login_empty_login_or_password_creds')]
        #                          )
    def test_login_courier_with_empty_login_or_password_fail(valid_login_or_password_creds):
        # my_fixture = request.getfixturevalue(courier_login_empty_login_or_password_creds)
        login_courier = LoginCourier()
        print('!!!!!!!!!', valid_login_or_password_creds)
        assert 1
            # response = login_courier.login_courier(payload)
            # assert response.status_code == 400
            # assert response.reason == 'Bad Request'
            # assert response.json()['code'] == 400
            # assert response.json()['message'] == "Недостаточно данных для входа"

