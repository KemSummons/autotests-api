import uuid
from pydantic import BaseModel, Field, ConfigDict


class ExerciseBase(BaseModel):
    """
    Базовые поля упражнения, общие для запросов и ответов.
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str = Field(..., min_length=1, max_length=250)
    max_score: int | None = Field(default=None, alias="maxScore")
    min_score: int | None = Field(default=None, alias="minScore")
    order_index: int = Field(default=0, alias="orderIndex")
    description: str = Field(..., min_length=1)
    estimated_time: str | None = Field(default=None, min_length=1, max_length=50, alias="estimatedTime")


class ExerciseSchema(ExerciseBase):
    """
    Описание структуры упражнения.
    """
    id: uuid.UUID
    course_id: uuid.UUID = Field(..., alias="courseId")


class GetExerciseResponseSchema(BaseModel):
    """
    Описание структуры ответа получения упражнения.
    """
    exercise: ExerciseSchema


class GetExercisesResponseSchema(BaseModel):
    """
    Описание структуры ответа получения упражнений.
    """
    exercises: list[ExerciseSchema]


class GetExercisesQuerySchema(BaseModel):
    """
    Описание структуры запроса на получение списка упражнений.
    """
    course_id: uuid.UUID = Field(..., alias="courseId")


class GetExerciseQuerySchema(BaseModel):
    """
    Описание структуры запроса на получение упражнения.
    """
    exercise_id: uuid.UUID


class CreateExerciseResponseSchema(BaseModel):
    """
    Описание структуры ответа на создание упражнения.
    """
    exercise: ExerciseSchema


class CreateExerciseRequestSchema(ExerciseBase):
    """
    Описание структуры запроса на создание упражнения.
    """
    course_id: uuid.UUID = Field(..., alias="courseId")


class UpdateExerciseResponseSchema(BaseModel):
    """
    Описание структуры ответа на обновление упражнения.
    """
    exercise: ExerciseSchema


class UpdateExerciseRequestSchema(ExerciseBase):
    """
    Описание структуры запроса на обновление упражнения.
    """
    title: str | None = Field(default=None, min_length=1, max_length=250)
    order_index: int | None = Field(default=None, alias="orderIndex")
    description: str | None = Field(default=None, min_length=1)
    estimated_time: str | None = Field(default=None, min_length=1, max_length=50, alias="estimatedTime")
