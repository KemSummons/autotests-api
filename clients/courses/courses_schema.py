import uuid
from pydantic import BaseModel, Field, ConfigDict
from clients.files.files_schema import FileSchema
from clients.users.users_schema import UserSchema


class CourseBase(BaseModel):
    """
    Базовые поля курса, общие для запросов и ответов.
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str = Field(..., min_length=1, max_length=250)
    max_score: int | None = Field(default=None, alias="maxScore")
    min_score: int | None = Field(default=None, alias="minScore")
    description: str = Field(..., min_length=1)
    estimated_time: str | None = Field(default=None, min_length=1, max_length=50, alias="estimatedTime")


class GetCoursesQuerySchema(BaseModel):
    """
    Описание структуры запроса на получение списка курсов.
    """
    model_config = ConfigDict(populate_by_name=True)

    user_id: uuid.UUID = Field(..., alias="userId")


class CreateCourseRequestSchema(CourseBase):
    """
    Описание структуры запроса на создание курса.
    """
    preview_file_id: uuid.UUID = Field(..., alias="previewFileId")
    created_by_user_id: uuid.UUID = Field(..., alias="createdByUserId")


class CourseSchema(CourseBase):
    """
    Описание структуры курса.
    """
    id: uuid.UUID
    preview_file: FileSchema = Field(alias="previewFile")
    created_by_user: UserSchema = Field(alias="createdByUser")


class CreateCourseResponseSchema(BaseModel):
    """
    Описание структуры ответ на создание курса
    """
    course: CourseSchema


class UpdateCourseRequestSchema(CourseBase):
    """
    Описание структуры запроса на обновление курса.
    """
    title: str | None = Field(default=None, min_length=1, max_length=250)
    max_score: int | None = Field(default=None, alias="maxScore")
    min_score: int | None = Field(default=None, alias="minScore")
    description: str | None = Field(default=None, min_length=1)
    estimated_time: str | None = Field(default=None, min_length=1, max_length=50, alias="estimatedTime")