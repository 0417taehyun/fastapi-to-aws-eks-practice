from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from src.constant import EndpointPrefix
from src.database import get_database_session
from src.model import HealthCheckModel, HealthCheckQueryModel
from src.service import HealthCheckService

router: APIRouter = APIRouter()


@router.get(path=EndpointPrefix.READYZ.value)
def check_readiness(session: Session = Depends(get_database_session)) -> JSONResponse:
    try:
        model: HealthCheckModel = HealthCheckModel(query_path_model=HealthCheckQueryModel)
        service: HealthCheckService = HealthCheckService(health_check_model=model)
        if service.is_database_connected(session=session):
            return JSONResponse(content={"detail": "Success"}, status_code=status.HTTP_200_OK)

        return JSONResponse(
            content={"detail": "Internal Server Error"},
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

    except Exception as error:
        return JSONResponse(
            content={"detail": f"Internal Server Error: {str(error)}"},
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


@router.get(path=EndpointPrefix.LIVEZ.value)
def check_liveness() -> JSONResponse:
    return JSONResponse(content={"detail": "Success"}, status_code=status.HTTP_200_OK)
