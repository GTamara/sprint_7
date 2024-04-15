import pytest

from data.create_order_data import CreateOrderData
from helper_functions.courier_helpers import CourierHelpers
from helper_functions.login_courier import LoginCourier
from helper_functions.order_helpers import OrderHelpers
from helper_functions.register_courier import RegisterCourier
from helper_functions.shared_helper_funcs import HelperFuncs


@pytest.fixture(scope="class")
def courier_login_valid_creds():
    register_courier = RegisterCourier()
    registered_courier_creds = register_courier.register_new_courier()
    login_courier = LoginCourier()
    courier_id = login_courier.get_courier_id(registered_courier_creds)
    yield registered_courier_creds, courier_id
    courier_helpers = CourierHelpers()
    courier_helpers.delete_couriers_by_id(courier_id)


@pytest.fixture(scope="class")
def courier_valid_login_and_incorrect_password(courier_login_valid_creds):
    return {
        'login': courier_login_valid_creds[0]['login'],
        'password': HelperFuncs.generate_random_string(8)
    }


@pytest.fixture(scope="class")
def courier_valid_password_and_incorrect_login(courier_login_valid_creds):
    return {
        'password': courier_login_valid_creds[0]['password'],
        'login': HelperFuncs.generate_random_string(8)
    }


@pytest.fixture(scope="class", params=['courier_valid_login', 'courier_valid_password'])
def courier_login_valid_login_and_password(request):
    return request.getfixturevalue(request.param)


@pytest.fixture(scope="class")
def created_order_data():
    order_helpers = OrderHelpers()
    payload = {
        **CreateOrderData.DEFAULT_CREATE_ORDER_PAYLOAD,
        'phone': HelperFuncs.generate_random_phone(),
        'deliveryDate': HelperFuncs.get_tomorrow_date()
    }
    resp = order_helpers.create_order_request(CreateOrderData.DEFAULT_CREATE_ORDER_PAYLOAD)
    order_track = order_helpers.get_order_track(resp)
    order_data = order_helpers.get_order_data(order_track)
    yield (order_track, order_data)
    order_helpers.cancel_order(order_track)
