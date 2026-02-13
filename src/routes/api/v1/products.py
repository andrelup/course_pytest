from  fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.db.async_session import get_session

router = APIRouter(prefix="/products", tags=["products"])

@router.get("/{id}")
async def get_product(id: int, session: AsyncSession = Depends(get_session)):
    # Aquí iría la lógica para obtener el producto de la base de datos usando el session
    return {"id": id, "name": "Producto de ejemplo"}
