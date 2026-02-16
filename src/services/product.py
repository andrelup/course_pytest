
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
        # Aquí iría la lógica para crear un nuevo producto en la base de datos usando el session
        return instance