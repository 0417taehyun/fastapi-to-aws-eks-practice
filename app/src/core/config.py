from functools import lru_cache

from pydantic import BaseSettings


class DatabaseSettings(BaseSettings):
    DATABASE_HOST: str
    DATABASE_PORT: str
    DATABASE_NAME: str
    DATABASE_USER: str
    DATABASE_PASSWORD: str

    @property
    def DATABASE_URL(self) -> str:
        USER_INFORMATION: str = ":".join([self.DATABASE_USER, self.DATABASE_PASSWORD])
        DATABASE_INFORMATION: str = ":".join([self.DATABASE_HOST, self.DATABASE_PORT])
        return f"mysql+mysqldb://{USER_INFORMATION}@{DATABASE_INFORMATION}/{self.DATABASE_NAME}?charset=utf8"


class ApplicationSettings(DatabaseSettings):
    pass


@lru_cache
def get_settings() -> ApplicationSettings:
    return ApplicationSettings()
