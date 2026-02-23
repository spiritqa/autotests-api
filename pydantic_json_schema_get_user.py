from clients.private_http_builder import AuthenticationUserSchema
from clients.users.private_users_client import get_private_users_client
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema, GetUserResponseSchema
from tools.assertions.schema import validate_json_schema
from tools.fakes import get_randome_email

public_users_client = get_public_users_client()

create_user_request = CreateUserRequestSchema(
    email=get_randome_email(),
    password="string",
    last_name="string",
    first_name="string",
    middle_name="string"
)

create_user_response = public_users_client.create_user(create_user_request)
print('Create user data: ',create_user_response)

authentication_user = AuthenticationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password
)
private_users_client = get_private_users_client(authentication_user).get_user_api(create_user_response.user.id)
private_users_client_schema = GetUserResponseSchema.model_json_schema()


validate_json_schema(instance=private_users_client.json(), schema=private_users_client_schema)