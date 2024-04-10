import json

import allure
import requests
from requests import Response

from constants.urls import Urls


class LoginCourier:

    @staticmethod
    @allure.step('Логин курьера с данными {payload}')
    def login_courier(payload: dict[str, str]) -> Response:
        response = requests.post(
            Urls.HOST + Urls.COURIER_LOGIN_PATH,
            data=json.dumps(payload),
            headers={'Content-Type': 'application/json; charset=utf-8'}
        )
        return response

    @allure.step('Получить логин курьера')
    def get_courier_id(self, login_creds: dict[str, str]) -> int:
        return self.login_courier(login_creds).json()['id']


