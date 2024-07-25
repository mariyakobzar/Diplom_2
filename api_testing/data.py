class Urls():

    URL = "https://stellarburgers.nomoreparties.site"

    CREATE_USER = '/api/auth/register'
    LOGIN_USER = '/api/auth/login'
    UPDATE_USER = '/api/auth/user'


    CREATE_ORDER = '/api/orders'
    GET_INGREDIENTS = "/api/ingredients"
    GET_ORDERS = "/api/orders/all"
    GET_ORDERS_USER = "/api/orders"

    DELETE_USER = "/api/auth/user"

    BUNS = {
        "bun_1": "61c0c5a71d1f82001bdaaa6d",
        "bun_2": "61c0c5a71d1f82001bdaaa6c"
    }

    MAIN = {
        "main_1": "61c0c5a71d1f82001bdaaa6f",
        "main_2": "61c0c5a71d1f82001bdaaa70",
        "main_3": "61c0c5a71d1f82001bdaaa71",
        "main_4": "61c0c5a71d1f82001bdaaa6e",
        "main_5": "61c0c5a71d1f82001bdaaa76",
        "main_6": "61c0c5a71d1f82001bdaaa77",
        "main_7": "61c0c5a71d1f82001bdaaa78",
        "main_8": "61c0c5a71d1f82001bdaaa79",
        "main_9": "61c0c5a71d1f82001bdaaa7a"
    }

    SAUCE = {
        "sauce_1": "61c0c5a71d1f82001bdaaa72",
        "sauce_2": "61c0c5a71d1f82001bdaaa73",
        "sauce_3": "61c0c5a71d1f82001bdaaa74",
        "sauce_4": "61c0c5a71d1f82001bdaaa75"
    }

class Responses:

    USER_ALREADY_EXISTS = '{"success":false,"message":"User already exists"}'
    EMAIL_PASS_NAME_REQUIRED = '{"success":false,"message":"Email, password and name are required fields"}'
    EMAIL_PASS_INCORRECT = '{"success":false,"message":"email or password are incorrect"}'
    NO_AUTHORISATION = '{"success":false,"message":"You should be authorised"}'
    USER_WITH_SUCH_EMAIL_ALREADY_EXISTS = '{"success":false,"message":"User with such email already exists"}'