from fastapi import APIRouter
from src.constant import APIVersionPrefix

router: APIRouter = APIRouter(prefix=APIVersionPrefix.V1.value)
