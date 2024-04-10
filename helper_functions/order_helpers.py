import json

import allure
import requests
from requests import Response

from constants.urls import Urls


class OrderHelpers:
    headers = {'Content-Type': 'application/json; charset=utf-8'}

    @allure.step('Создать заказ с данными {payload}')
    def create_order_request(self, payload: dict[str, str | list[str] | int]) -> Response:
        response = requests.post(
            Urls.HOST + Urls.ORDER_BASE_PATH,
            data=json.dumps(payload),
            headers=self.headers
        )
        return response

    @allure.step('Отправить запрос на полученин данных заказа по треку {track}')
    def get_order_details_request(self, track: int | None) -> Response:
        response = requests.get(
            Urls.HOST + Urls.GET_ORDER_DETAILS_BY_TRACK_PATH,
            params={'t': track},
            headers=self.headers
        )
        return response

    @staticmethod
    @allure.step('Получить трек заказа')
    def get_order_track(resp: Response) -> int | None:
        if resp.status_code == 201:
            order_track = resp.json().get('track')
            return order_track
        else:
            raise Exception(f'Ошибка при создании заказа. Код ошибки {resp.status_code}')

    @staticmethod
    @allure.step('Получить id заказа')
    def get_order_id(order_data) -> int:
        order_id = order_data.get('order').get('id')
        return order_id

    @allure.step('Получить данные заказа по треку {track}')
    def get_order_data(self, track: int) -> dict | None:
        resp = requests.get(
            Urls.HOST + Urls.GET_ORDER_DETAILS_BY_TRACK_PATH,
            params={'t': track},
            headers=self.headers
        )
        if resp.status_code == 200:
            data = resp.json()
            return data
        else:
            raise Exception(f'Ошибка при получении данных заказа. Код ошибки {resp.status_code}')

    @staticmethod
    @allure.step('Отменить заказ по треку {track}')
    def cancel_order(track: int) -> Response:
        """
            Отменить заказ
            :return: Response
        """
        resp = requests.put(
            Urls.HOST + Urls.CANCEL_ORDER_PATH,
            params={
                'track': track
            }
        )
        return resp

    @staticmethod
    @allure.step('Принять заказ с id {order_id} курьером с courier_id {courier_id}')
    def accept_order(order_id: int | str, courier_id: int | None) -> Response:
        """
            Курьер принимает заказ
            :return: Response
        """
        resp = requests.put(
            Urls.HOST + f'{Urls.ACCEPT_ORDER_PATH}{order_id if bool(order_id) else ""}',
            params={
                'courierId': courier_id
            }
        )
        return resp

    @staticmethod
    @allure.step('Получить список заказов')
    def get_orders_list(params: dict | None) -> Response:
        """
            Получить список заказов
            :return: Response
        """
        response = requests.get(Urls.HOST + Urls.ORDER_BASE_PATH, params=params)
        return response
