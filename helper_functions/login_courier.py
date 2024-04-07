import requests

from constants.urls import Urls


class LoginCourier:

    def login_courier(self, payload: dict[str, str]): # _and_return_login_password
        response = requests.post( Urls.HOST + '/api/v1/courier/login', data=payload)
        return response

    def get_courier_id(self, login_creds: dict[str, str]):
        return self.login_courier(login_creds).json()['id']

    def get_invalid_login_or_password_payload_list(self, valid_login: str, valid_password: str):
        return [
            { 'login': valid_login },
            { 'password': valid_password },
            { 'login': valid_login, 'password': '' },
            { 'login': '', 'password': valid_password },
            {}
        ]


