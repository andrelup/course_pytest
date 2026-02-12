from fastapi import FastAPI

from src.routes.base_route import base_commons

app = FastAPI()
app.include_router(base_commons)