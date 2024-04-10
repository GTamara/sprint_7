import allure

from helper_functions.order_helpers import OrderHelpers
from constants.response_error_messages import ResponseErrorMessages


class TestOrderDetails():

    @allure.title('Получить данные заказа. Если передан трек существующего заказа, успешно')
    def test_get_order_details_with_existing_track_success(self, created_order_data):
        track = created_order_data[0]
        order_helpers = OrderHelpers()
        response = order_helpers.get_order_details_request(track)
        assert response.status_code == 200
        assert response.reason == 'OK'
        assert 'order' in response.json()
        assert type(
            response.json()['order']
        ) == dict

    @allure.title('Получить данные заказа. Если НЕ передан трек существующего заказа, НЕ успешно')
    def test_get_order_details_without_track_fail(self):
        track = None
        order_helpers = OrderHelpers()
        response = order_helpers.get_order_details_request(track)
        assert response.status_code == 400
        assert response.reason == 'Bad Request'
        assert response.json()['message'] == ResponseErrorMessages.NOT_ENOUGH_DATA_FOR_SEARCHING

    @allure.title('Получить данные заказа. Если передан трек НЕ существующего заказа, НЕ успешно')
    def test_get_order_details_with_not_existing_track_fail(self, created_order_data):
        track = created_order_data[0]
        order_helpers = OrderHelpers()
        order_helpers.cancel_order(track)
        response = order_helpers.get_order_details_request(track)
        assert response.status_code == 404
        assert response.reason == 'Not Found'
        assert response.json()['message'] == ResponseErrorMessages.ORDER_NOT_FOUND


