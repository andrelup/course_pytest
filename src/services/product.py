
from sqlalchemy import select
from src.models.product import ProductModel


class ProductService:
    
    async def get_by_id(self, session, id: int) -> ProductModel:
        stmt = select(ProductModel).where(ProductModel.id == id)
        result = await session.execute(stmt)
        return result.scalars().first()

    async def create(self, session, name: str, price: float) -> ProductModel:
        instance = ProductModel(name=name, price=price)
        try:
            session.add(instance)
            await session.commit()
            await session.refresh(instance)
        except Exception as e:
            await session.rollback()
            raise e
        return instance
    
    async def modify(self, session, id: int, **fields) -> ProductModel:
        instance = await self.get_by_id(session, id)
        if not instance:
            return False
        for field, value in fields.items():
            setattr(instance, field, value)

        await session.commit()
        await session.refresh(instance)
        return instance
    
    async def delete(self, session, id: int) -> ProductModel:
        instance = await self.get_by_id(session, id)
        if not instance:
            return False
        
        session.delete(instance)
        await session.commit()
        return instance