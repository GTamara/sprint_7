import json
import requests
from requests import Response

from constants.urls import Urls


class LoginCourier:

    @staticmethod
    def login_courier(payload: dict[str, str]):
        response = requests.post(
            Urls.HOST + '/api/v1/courier/login',
            data=json.dumps(payload),
            headers={'Content-Type': 'application/json; charset=utf-8'}
        )
        return response

    def get_courier_id(self, login_creds: dict[str, str]):
        return self.login_courier(login_creds).json()['id']

    @staticmethod
    def get_courier_id_from_response(response: Response):
        return response.json()['id']


