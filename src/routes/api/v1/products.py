from  fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from src.db.async_session import get_session
from src.models.product import BaseProductModel, OptionalProductModel, ProductModel
from src.services.product import ProductService


router = APIRouter(prefix="/products", tags=["products"])

@router.get("/{id}", response_model=ProductModel)
async def get_product_by_id(id: int, session: AsyncSession = Depends(get_session), product_service = Depends(ProductService)):
    instance = await product_service.get_by_id(session, id)
    if not instance:
        raise HTTPException(status_code=404, detail=f"Product with ID {id} not found")
    return instance

@router.post("/", response_model=ProductModel, status_code=status.HTTP_201_CREATED)
async def create_new_product(payload: BaseProductModel, session: AsyncSession = Depends(get_session), product_service = Depends(ProductService)):
    return await product_service.create(session, name=payload.name, price=payload.price)

@router.patch("/{id}", response_model=ProductModel)
async def modify_partial(id: int, payload: OptionalProductModel, session: AsyncSession = Depends(get_session), product_service = Depends(ProductService)):
    instance = await product_service.modify(session, id, **payload.dict(exclude_unset=True))
    if not instance:
        raise HTTPException(status_code=404, detail=f"Product with ID {id} not found")
    return instance

@router.put("/{id}", response_model=ProductModel)
async def modify_total(id: int, payload: BaseProductModel, session: AsyncSession = Depends(get_session), product_service = Depends(ProductService)):
    instance = await product_service.modify(session, id=id, name=payload.name, price=payload.price)
    if not instance:
        raise HTTPException(status_code=404, detail=f"Product with ID {id} not found")
    return instance

@router.delete("/{id}", response_model=ProductModel)
async def delete_product(id: int, session: AsyncSession = Depends(get_session), product_service = Depends(ProductService)):
    instance = await product_service.delete(session, id)
    if not instance:
        raise HTTPException(status_code=404, detail=f"Product with ID {id} not found")
    return instance

