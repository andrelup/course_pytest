
from datetime import datetime
from typing import Optional

from sqlalchemy import Column, DateTime, func
from sqlmodel import Field, SQLModel


class BaseModel(SQLModel):
    id:Optional[int] = Field(default=None, primary_key=True)
    created_at: Optional[datetime] = Field(
        sa_column=Column(DateTime, server_default=func.now(), nullable=True)    
    )
    updated_at: Optional[datetime] = Field(
        sa_column=Column(DateTime, onupdate=func.now(), nullable=True)    
    )