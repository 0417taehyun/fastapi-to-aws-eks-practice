from fastapi import APIRouter
from src.router import check

router: APIRouter = APIRouter()


router.include_router(router=check.router)
