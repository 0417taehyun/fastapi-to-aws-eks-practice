from sqlalchemy.orm import Session

from src.model import HealthCheckModel


class HealthCheckService:
    def __init__(self, health_check_model: HealthCheckModel) -> None:
        self.health_check_model: HealthCheckModel = health_check_model

    def is_database_connected(self, session: Session) -> bool:
        return bool(self.health_check_model.check_database_connection(session=session).get("flag"))
