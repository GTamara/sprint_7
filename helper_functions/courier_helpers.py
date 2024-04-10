import allure
import requests
from requests import Response

from constants.urls import Urls


class CourierHelpers:

    @staticmethod
    @allure.step('Удалить курьера по id')
    def delete_couriers_by_id(courier_id: str | int) -> Response:
        url = f"{Urls.HOST}{Urls.COURIER_BASE_PATH}/{courier_id}"
        return requests.delete(url=url)