import requests
from requests import Response

from constants.urls import Urls


class CourierHelpers:

    @staticmethod
    def delete_couriers_by_id(courier_id: str | int) -> Response:
        url = f"{Urls.HOST}/api/v1/courier/{courier_id}"
        return requests.delete(url=url)