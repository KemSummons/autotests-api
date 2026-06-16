import uuid
from pydantic import BaseModel, Field, HttpUrl


class FileSchema(BaseModel):
    """
    Описание структуры файла.
    """
    id: uuid.UUID
    url: HttpUrl = Field(..., min_length=1, max_length=2083)
    filename: str = Field(..., max_length=250)
    directory: str = Field(..., max_length=250)

# Добавили описание структуры ответа на создание файла
class CreateFileResponseSchema(BaseModel):
    """
    Описание структуры ответа создания файла.
    """
    file: FileSchema


class CreateFileRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание файла.
    """
    filename: str = Field(..., min_length=1, max_length=255)
    directory: str = Field(..., min_length=1, max_length=1024)
    upload_file: str