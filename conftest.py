import pytest

from data.create_order_data import CreateOrderData
from helper_functions.delete_courier import DeleteCourier
from helper_functions.login_courier import LoginCourier
from helper_functions.order_helpers import OrderHelpers
from helper_functions.register_courier import RegisterCourier


@pytest.fixture(scope="class")
def courier_login_valid_creds():
    register_courier = RegisterCourier()
    # payload = register_courier.get_register_payload()

    registered_courier_creds = register_courier.register_new_courier()
    login_courier = LoginCourier()
    courier_id = login_courier.get_courier_id(registered_courier_creds)
    yield registered_courier_creds, courier_id
    delete_courier = DeleteCourier()
    delete_courier.delete_couriers_by_id(courier_id)


@pytest.fixture(scope="class")
def created_order_data():
    order_helpers = OrderHelpers()
    resp = order_helpers.create_order_request(CreateOrderData.DEFAULT_CREATE_ORDER_PAYLOAD)
    order_track = order_helpers.get_order_track(resp)
    order_data = order_helpers.get_order_data(order_track)
    yield (order_track, order_data)
    order_helpers.cancel_order(order_track)


# @pytest.fixture(scope="class")
# def order_data_with_payload():
#     def core(payload):
#         order_helpers = OrderHelpers()
#         resp = order_helpers.create_order_request(payload)
#         order_track = order_helpers.get_order_track(resp)
#         order_data = order_helpers.get_order_data(resp)
#         yield order_track, order_data
#         order_helpers.cancel_order(order_track)
#     return core



@pytest.fixture
def addition():
    def core(num1, num2):
        return num1 + num2
    return core

def test(request, addition):
    print(addition(2, 3))
    print(request.getfixturevalue("addition")(6, 8))
    assert True