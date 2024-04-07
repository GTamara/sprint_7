import json

import requests
from requests import Response

from constants.urls import Urls
from data.create_order_data import CreateOrderData


class OrderHelpers:

    def create_order_request(self, payload):
        response = requests.post(
            Urls.HOST + '/api/v1/orders',
            data=json.dumps(payload),
            headers={'Content-Type': 'application/json; charset=utf-8'}
        )
        return response

    def get_order_track(self, resp: Response):
        if resp.status_code == 201:
            order_track = resp.json().get('track')
            return order_track
        else:
            raise Exception(f'Ошибка при создании заказа. Код ошибки {resp.status_code}')

    def get_order_id(self, order_data):
        order_id = order_data.get('order').get('id')
        return order_id

    def get_order_data(self, track: int):
        resp = requests.get(
            Urls.HOST + '/api/v1/orders/track',
            params={'t': track},
            headers={'Content-Type': 'application/json; charset=utf-8'}
        )
        if resp.status_code == 200:
            data = resp.json()
            return data
        else:
            raise Exception(f'Ошибка при получении данных заказа. Код ошибки {resp.status_code}')

    def cancel_order(self, track: int):
        """
            Отменить заказ
            :return: Response
        """
        resp = requests.put(
            Urls.HOST + '/api/v1/orders/cancel',
            params={
                'track': track
            }
        )
        return resp

    def accept_order(self, order_id: int | str, courier_id: int | None):
        """
            Курьер принимает заказ
            :return: Response
        """
        resp = requests.put(
            Urls.HOST + f'/api/v1/orders/accept/{order_id if bool(order_id) else ""}',
            params={
                'courierId': courier_id
            }
        )
        return resp

    def get_orders_list(self, params: dict | None): # _and_return_login_password
        response = requests.get( Urls.HOST + '/api/v1/orders', params=params)
        return response
