from fastapi import APIRouter

from src.routes.api.commons import router as commons_router
from src.routes.api.v1.products import router as products_router

base_commons = APIRouter(prefix="/commons")
base_commons.include_router(commons_router)

base_v1 = APIRouter(prefix="/v1")
base_v1.include_router(products_router)