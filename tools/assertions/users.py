from clients.users.users_schema import CreateUserRequestSchema,CreateUserResponseSchema,GetUserResponseSchema,UserSchema
from tools.assertions.base import assert_equal

def assert_create_user_response(request: CreateUserRequestSchema, response: CreateUserResponseSchema):
    """
    Проверяет, что ответ на создание пользователя соответствует запросу.

    :param request: Исходный запрос на создание пользователя.
    :param response: Ответ API с данными пользователя.
    :return AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(response.user.email, request.email, "email")
    assert_equal(response.user.last_name, request.last_name, "last_name")
    assert_equal(response.user.middle_name, request.middle_name, "middle_name")
    assert_equal(response.user.first_name, request.first_name, "first_name")


def assert_user(request: UserSchema, response: UserSchema):
    """
    Проверяет корректность данных пользователя.

    :param request: Запрос с данными текущего пользователя
    :param response: Ответ с данными созданного пользователя
    :return AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(request.id, response.id, "id")
    assert_equal(request.email, response.email, "email")
    assert_equal(request.last_name, response.last_name, "last_name")
    assert_equal(request.middle_name, response.middle_name, "middle_name")
    assert_equal(request.first_name, response.first_name, "first_name")


def assert_get_user_response(get_user_response: GetUserResponseSchema, create_user_response: CreateUserResponseSchema):
    """
    Проверяет , что данные пользователя при создании и при запросе совпадают.

    :param get_user_response: Ответ API при запросе пользователя
    :param create_user_response: Ответ API при создании пользователя
    :return AssertionError: Если данные пользователя не совпадают
    """
    assert_user(get_user_response.user, create_user_response.user)
