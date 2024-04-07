import datetime
import random
import string


class HelperFuncs:
    def generate_random_string(length: int) -> str:
        letters = string.ascii_lowercase + string.digits
        rand_string = ''.join(random.choice(letters) for i in range(length))
        return rand_string

    @staticmethod
    def get_tomorrow_date():
        today = datetime.date.today()
        tomorrow_date = today + datetime.timedelta(days=1)
        return str(tomorrow_date)

    @staticmethod
    def generate_random_phone():
        phone = '+7' + (''.join(random.choice(string.digits) for i in range(10)))