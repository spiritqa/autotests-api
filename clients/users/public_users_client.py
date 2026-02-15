from httpx import Response

from clients.api_client import APIClient
from typing import TypedDict

class CreateUserDict(TypedDict):
    """
    Описание структуры запроса для создания нового клиента.
    """
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str

class PublicUsersClient(APIClient):
    """
    Клиент для работы с /api/v1/users
    """
    def create_user_api(self, request: CreateUserDict)-> Response:
        """
        Метод создания нового клиента.

        :param request: Словарь с параметрами: email, password. LastName, firstName, middleName.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/users", json=request)