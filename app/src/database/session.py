from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import Session, sessionmaker

from src.core import get_settings

_engine: Engine = create_engine(url=get_settings().DATABASE_URL)
_session: sessionmaker = sessionmaker(bind=_engine)


def get_database_session() -> Session:
    with _session() as session:
        yield session
