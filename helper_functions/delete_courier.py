import requests
from requests import Response

from  constants.urls import Urls


class DeleteCourier:

    def delete_couriers_by_id(self, courier_id: str | int) -> Response:
        url = f"{Urls.HOST}/api/v1/courier/{ courier_id }"
        return requests.delete(url=url)
        # resp = requests.get(Urls.HOST + Urls.COURIERS_TABLE_PATH)

