from fastapi import APIRouter

from src.routes.api.commons import router as commons_router

base_commons = APIRouter(prefix="/commons")
base_commons.include_router(commons_router)