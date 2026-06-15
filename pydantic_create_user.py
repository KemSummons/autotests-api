import uuid
from pydantic import BaseModel, Field, EmailStr, ConfigDict


class UserBase(BaseModel):
    """
    Базовые поля пользователя, общие для запросов и ответов.

    Attributes:
        email: Электронная почта пользователя.
        last_name: Фамилия пользователя.
        first_name: Имя пользователя.
        middle_name: Отчество пользователя.
    """
    model_config = ConfigDict(populate_by_name=True)

    email: EmailStr = Field(..., max_length=250)
    last_name: str = Field(..., min_length=1, max_length=50, alias="lastName")
    first_name: str = Field(..., min_length=1, max_length=50, alias="firstName")
    middle_name: str = Field(..., min_length=1, max_length=50, alias="middleName")


class UserSchema(UserBase):
    """
    Модель данных пользователя.

    Attributes:
        id: Уникальный идентификатор пользователя.
    """
    id: uuid.UUID


class CreateUserRequestSchema(UserBase):
    """
    Модель запроса на создание пользователя.

    Attributes:
        password: Пароль пользователя.
    """
    password: str = Field(..., min_length=1, max_length=250)


class CreateUserResponseSchema(BaseModel):
    """
    Модель ответа с данными созданного пользователя.

    Attributes:
        user: Объект данных пользователя.
    """
    user: UserSchema