from enum import Enum
from pathlib import Path
from typing import Protocol, TypeVar

from pydantic import FilePath
from sqlalchemy import TextClause, text

from src.constant import BaseQueryFilePath
from src.database import Base

T = TypeVar("T", bound=Enum, contravariant=True)


class BaseQueryModel(Protocol[T]):
    _BASE_PATH: FilePath = Path(BaseQueryFilePath.BASE_PATH.value)
    DIRECTORY: Enum

    @classmethod
    def get_query(cls: "BaseQueryModel", query_name: T) -> TextClause:
        file_path: FilePath = cls._BASE_PATH.joinpath(cls.DIRECTORY.value, query_name.value)
        with open(file=file_path) as file:
            return text(text=file.read())


class PlainBaseModel:
    def __init__(self, query_path_model: BaseQueryModel[T]) -> None:
        self.query_path_model: BaseQueryModel[T] = query_path_model


class BaseModel(PlainBaseModel):
    def __init__(self, query_path_model: BaseQueryModel[T], model: Base) -> None:
        super().__init__(query_path_model=query_path_model)
        self.model: Base = model
