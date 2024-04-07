from helper_functions.order_helpers import OrderHelpers


class TestAcceptOrder:

    def test_accept_order_with_existing_courier_id_order_id_success(
            self,
            courier_login_valid_creds,
            created_order_data,
    ):
        order_helpers = OrderHelpers()
        order_id = order_helpers.get_order_id(created_order_data[1])
        courier_id = courier_login_valid_creds[1]
        resp = order_helpers.accept_order(
            order_id,
            courier_id,
        )
        assert resp.status_code == 200
        assert resp.reason == 'OK'
        assert resp.json().get('ok') == True

    def test_accept_order_with_empty_courier_id_fail(
            self,
            created_order_data,
    ):
        order_helpers = OrderHelpers()
        order_id = order_helpers.get_order_id(created_order_data[1])
        # courier_id = courier_login_valid_creds[1]
        resp = order_helpers.accept_order(
            order_id,
            None,
        )
        assert resp.status_code == 400
        assert resp.reason == 'Bad Request'
        assert resp.json().get('message') == "Недостаточно данных для поиска"

    def test_accept_order_with_empty_order_id_fail(
            self,
            courier_login_valid_creds,
    ):
        courier_id = courier_login_valid_creds[1]
        order_helpers = OrderHelpers()
        resp = order_helpers.accept_order(
            None,
            courier_id,
        )
        assert resp.status_code == 400
        assert resp.reason == 'Bad Request'
        assert resp.json().get('message') == "Недостаточно данных для поиска"

    def test_accept_order_with_not_existing_order_id_fail(
            self,
            courier_login_valid_creds,
            created_order_data,
    ):
        courier_id = courier_login_valid_creds[1]
        order_helpers = OrderHelpers()
        order_id = order_helpers.get_order_id(created_order_data[1])
        order_helpers.cancel_order(created_order_data[0])
        resp = order_helpers.accept_order(
            order_id,
            courier_id,
        )
        assert resp.status_code == 404
        assert resp.reason == 'Not Found'
        assert resp.json().get('message') == "Заказа с таким id не существует"

    def test_accept_order_with_not_existing_courier_id_fail(
            self,
            courier_login_valid_creds,
            created_order_data,
    ):
        courier_id = courier_login_valid_creds[1]
        order_helpers = OrderHelpers()
        order_id = order_helpers.get_order_id(created_order_data[1])
        order_helpers.cancel_order(created_order_data[0])
        resp = order_helpers.accept_order(
            courier_id,
            courier_id,
        )
        assert resp.status_code == 404
        assert resp.reason == 'Not Found'
        assert resp.json().get('message') == "Заказа с таким id не существует"

    def test_accept_order_with_accepted_order_id_fail(
            self,
            courier_login_valid_creds,
            created_order_data,
    ):
        courier_id = courier_login_valid_creds[1]
        order_helpers = OrderHelpers()
        order_id = order_helpers.get_order_id(created_order_data[1])
        # order_helpers.cancel_order(created_order_data[0])
        order_helpers.accept_order(
            order_id,
            courier_id,
        )
        resp = order_helpers.accept_order(
            order_id,
            courier_id,
        )
        assert resp.status_code == 409
        assert resp.reason == 'Conflict'
        assert resp.json().get('message') == "Этот заказ уже в работе"
