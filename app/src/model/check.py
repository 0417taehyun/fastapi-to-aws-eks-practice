from sqlalchemy import Row, TextClause
from sqlalchemy.orm import Session

from src.constant import HealthCheckQuery
from src.custom import CheckDatabaseConnectionRow
from src.model.base import BaseQueryModel, PlainBaseModel


class HealthCheckQueryModel(BaseQueryModel):
    DIRECTORY = HealthCheckQuery.DIRECTORY


class HealthCheckModel(PlainBaseModel):
    def check_database_connection(self, session: Session) -> CheckDatabaseConnectionRow:
        statement: TextClause = self.query_path_model.get_query(query_name=HealthCheckQuery.READINESS)
        row: Row = session.execute(statement=statement).fetchone()
        return row._mapping
