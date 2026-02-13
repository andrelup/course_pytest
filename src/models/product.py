

from datetime import datetime
from typing import Optional
from sqlmodel import Field, SQLModel

from src.models.base import BaseModel

class OptionalProductModel(SQLModel):
    name: Optional[str] 
    price: Optional[float]

class BaseProductModel(SQLModel):
    name: str 
    price: float

class ProductModel(BaseProductModel, BaseModel, table=True):
    pass