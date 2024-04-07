from helper_functions.order_helpers import OrderHelpers


class TestOrdersList:

    def test_get_orders_list_without_filters(self):
        order_helpers = OrderHelpers()
        response = order_helpers.get_orders_list(None)
        assert response.status_code == 200
        assert response.reason == 'OK'
        assert 'orders' in response.json()
        assert type(
            response.json()['orders']
        ) == list

