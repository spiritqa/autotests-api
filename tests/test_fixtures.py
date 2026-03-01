import pytest



@pytest.fixture(autouse=True)
def send_analytics_data():
    print("[AUTOUSE] Отправляем данные в сервис аналитики")

@pytest.fixture(scope="session")
def setting():
    print("[SESSION] Инициализируем настройки автотестов")

@pytest.fixture(scope="class")
def user():
    print("[CLASS] Создаем данные пользователя один раз на тестовый класс")

@pytest.fixture(scope="function")
def user_client(setting):
    print("[FUNCTION] Создаем API клиент на каждый автотест")



class TestUserFlow:
    def test_user_can_login(self, setting, user, user_client):
        ...


    def test_user_can_create_course(self, setting, user, user_client):
        ...



class TestAccountFlow:
    def test_user_account(self, setting, user, user_client):
        ...


@pytest.fixture
def user_data() -> dict:
    print('Создаем пользователя до теста(setup)')
    yield {"username":"test_user", "email":"test@example.com"}
    print('Удаляем пользователя после теста(teardown)')


def test_user_email(user_data: dict):
    print(user_data)
    assert user_data['email'] == 'test@example.com'


def test_user_name(user_data: dict):
    print(user_data)
    assert user_data['username'] == 'test_user'