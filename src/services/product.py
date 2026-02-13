
from src.models.product import ProductModel


class ProductService:
    
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