from fastapi import APIRouter

router = APIRouter()

@router.get("/healthcheck")
async def healthcheck():
    return {"status": "on"}

@router.get("/environment")
async def environment():
    return {"environment": "local"}

