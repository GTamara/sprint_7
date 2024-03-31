import requests
import helper_funcs
from constants.urls import Urls

class RegisterCourier:

    def get_register_payload(self):
        # генерируем логин, пароль и имя курьера
        login = helper_funcs.generate_random_string(10)
        password = helper_funcs.generate_random_string(10)
        first_name = helper_funcs.generate_random_string(10)

        return {
            "login": login,
            "password": password,
            "firstName": first_name
        }

    # метод регистрации нового курьера возвращает список из логина и пароля
    # если регистрация не удалась, возвращает пустой список
    def register_new_courier(self, payload): # _and_return_login_password
        # собираем тело запроса
        # payload = self.get_register_payload()

        # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
        response = requests.post( Urls.HOST + '/api/v1/courier', data=payload)

        # если регистрация прошла успешно (код ответа 201), добавляем в список логин и пароль курьера
        # if response.status_code == 201:
        #     login_pass.append(login)
        #     login_pass.append(password)
        #     login_pass.append(first_name)
        #
        # # возвращаем список
        # return login_pass
        return response