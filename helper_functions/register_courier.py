import requests
from requests import Response

from constants.urls import Urls
from helper_functions.shared_helper_funcs import HelperFuncs


class RegisterCourier:

    @staticmethod
    def get_register_payload() -> dict[str, str]:
        login = HelperFuncs.generate_random_string(10)
        password = HelperFuncs.generate_random_string(10)
        first_name = HelperFuncs.generate_random_string(10)

        return {
            "login": login,
            "password": password,
            "firstName": first_name
        }

    @staticmethod
    def register_new_courier_request(payload: dict[str, str]) -> Response:
        response = requests.post( Urls.HOST + '/api/v1/courier', data=payload)
        return response

    def register_new_courier(self) -> dict[str, str]:
        payload = self.get_register_payload()
        response = self.register_new_courier_request(payload)
        if response.status_code == 201:
            return payload
        else:
            raise Exception('Произошла ошибка при регистрации курьера')