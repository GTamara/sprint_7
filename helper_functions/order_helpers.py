import json

import requests
from requests import Response

from constants.urls import Urls


class OrderHelpers:

    @staticmethod
    def create_order_request(payload):
        response = requests.post(
            Urls.HOST + '/api/v1/orders',
            data=json.dumps(payload),
            headers={'Content-Type': 'application/json; charset=utf-8'}
        )
        return response

    @staticmethod
    def get_order_details_request(track: int | None):
        response = requests.get(
            Urls.HOST + '/api/v1/orders/track',
            params={ 't': track },
            headers={'Content-Type': 'application/json; charset=utf-8'}
        )
        return response

    @staticmethod
    def get_order_track(resp: Response):
        if resp.status_code == 201:
            order_track = resp.json().get('track')
            return order_track
        else:
            raise Exception(f'Ошибка при создании заказа. Код ошибки {resp.status_code}')

    @staticmethod
    def get_order_id(order_data):
        order_id = order_data.get('order').get('id')
        return order_id

    @staticmethod
    def get_order_data(track: int):
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

    @staticmethod
    def cancel_order(track: int):
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

    @staticmethod
    def accept_order(order_id: int | str, courier_id: int | None):
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

    @staticmethod
    def get_orders_list(params: dict | None):
        """
            Получить список заказов
            :return: Response
        """
        response = requests.get( Urls.HOST + '/api/v1/orders', params=params)
        return response
