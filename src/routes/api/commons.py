from fastapi import APIRouter

from src.settings.environment import EnvironmentSettings

router = APIRouter()

@router.get("/healthcheck")
async def healthcheck():
    return {"status": "on"}

@router.get("/environment")
async def environment():
    return {"environment": EnvironmentSettings.ENVIRONMENT}

