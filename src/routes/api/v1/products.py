from  fastapi import APIRouter, Depends, Response
from sqlalchemy.ext.asyncio import AsyncSession
from src.db.async_session import get_session
from src.models.product import BaseProductModel, OptionalProductModel, ProductModel
from src.services.product import ProductService


router = APIRouter(prefix="/products", tags=["products"])

@router.get("/{id}", response_model=ProductModel)
async def get_product_by_id(id: int, session: AsyncSession = Depends(get_session)):
    # Aquí iría la lógica para obtener el producto de la base de datos usando el session
    return {"id": id, "name": "Producto de ejemplo"}

@router.post("/", response_model=ProductModel)
async def create_new_product(payload: BaseProductModel, session: AsyncSession = Depends(get_session), product_service = Depends(ProductService)):
    # Aquí iría la lógica para crear un nuevo producto en la base de datos usando el session
    return await product_service.create(session, name=payload.name, price=payload.price)

@router.patch("/{id}", response_model=ProductModel)
async def modify_partial(id: int, payload: OptionalProductModel, session: AsyncSession = Depends(get_session)):
    # Aquí iría la lógica para actualizar parcialmente un producto existente en la base de datos usando el session
    return {"id": id, "name": payload.name}

@router.put("/{id}", response_model=ProductModel)
async def modify_total(id: int, payload: BaseProductModel, session: AsyncSession = Depends(get_session)):
    # Aquí iría la lógica para actualizar un producto existente en la base de datos usando el session
    return {"id": id, "name": payload.name}

@router.delete("/{id}", response_model=ProductModel)
async def delete_product(id: int, session: AsyncSession = Depends(get_session)):
    # Aquí iría la lógica para eliminar un producto de la base de datos usando el session
    return {"id": id, "name": "Producto eliminado"}

