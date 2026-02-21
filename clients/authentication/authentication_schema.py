from pydantic import BaseModel,Field, EmailStr



class TokenSchema(BaseModel):
    """
    Описание структуры запроса на данные токена.
    """
    token_type: str = Field(alias="tokenType")
    access_token: str = Field(alias="accessToken")
    refresh_token: str = Field(alias="refreshToken")

class LoginRequestSchema(BaseModel):
    """
    Описание структуры запроса на аутентификацию.
    """
    email: str
    password: str

class LoginResponseSchema(BaseModel):
    """
    Описание структуры запроса на значение токена.
    """
    token: TokenSchema

class RefreshRequestSchema(BaseModel):
    """
    Описание структуры запроса для обновления токена.
    """
    refresh_token: str = Field(alias="refreshToken")