import allure
import pytest

from data.create_order_data import CreateOrderData
from helper_functions.order_helpers import OrderHelpers


class TestCreateOrder:

    @allure.title('Создание заказа. Если список цветов: {colors_list}, успешно')
    @pytest.mark.parametrize(
        'colors_list',
        CreateOrderData.COLORS_LIST
    )
    def test_create_order_with_color_params_success(self, colors_list: list | list[str] | None):
        payload = {
            **CreateOrderData.DEFAULT_CREATE_ORDER_PAYLOAD,
            'color': colors_list
        }
        order_helpers = OrderHelpers()
        response = order_helpers.create_order_request(payload)
        assert response.status_code == 201
        assert response.reason == 'Created'
        assert 'track' in response.json()
        assert type(
            response.json()['track']
        ) == int



