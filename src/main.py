from fastapi import FastAPI

from src.routes.base_router import base_commons, base_v1

app = FastAPI()
app.include_router(base_commons)
app.include_router(base_v1)