from enum import Enum


class BaseQueryFilePath(str, Enum):
    BASE_PATH: str = "src/sql"


class HealthCheckQuery(str, Enum):
    DIRECTORY: str = "check"
    READINESS: str = "readiness.sql"
