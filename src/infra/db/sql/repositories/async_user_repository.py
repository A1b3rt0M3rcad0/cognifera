from sqlalchemy.future import select
from sqlalchemy import update
from src.infra.db.sql.interfaces.i_async_db_connection_handler import IAsyncDBConnectionHandler
from src.data.interfaces.i_aynsc_user_repository import IAsyncUserRepository
from src.domain.models.user import User
from src.infra.db.sql.entities.user import User as UserEntity
from typing import Dict

class AsyncUserRepository(IAsyncUserRepository):

    def __init__(self, db_connection_handler: IAsyncDBConnectionHandler) -> None:
        self.__db_connection_handler = db_connection_handler
    
    async def insert(self, email: str, username: str, password: str, flash_card_generated_in_the_month: int) -> None:
        async with self.__db_connection_handler as db:
            try:
                user = UserEntity(
                    email=email, 
                    username=username, 
                    password=password, 
                    flash_card_generated_in_the_month=flash_card_generated_in_the_month,
                )
                db.session.add(user)
                await db.session.commit()
            except Exception as e:
                await db.session.rollback()
                raise e
    
    async def select(self, email: str) -> User:
        async with self.__db_connection_handler as db:
            try:
                result = await db.session.execute(
                    select(UserEntity).filter(UserEntity.email == email)
                )
                user = result.scalars().all()
                return user[0]
            except Exception as e:
                await db.session.rollback()
                raise e
    
    async def update(self, email: str, update_params: Dict) -> None:
        async with self.__db_connection_handler as db:
            try:

                stmt = update(UserEntity).where(UserEntity.email == email).values(update_params)      
                await db.session.execute(stmt)
                await db.session.commit()
            except Exception as e:
                await db.session.rollback()
                raise e
    
    async def delete(self, email: str) -> None:
        async with self.__db_connection_handler as db:
            try:
                stmt = select(UserEntity).where(UserEntity.email == email)
                result = await db.session.execute(stmt)
                user = result.scalar_one_or_none()
                if user:
                    await db.session.delete(user)
                    await db.session.commit()
                else:
                    raise RuntimeError(f'The user with email "{email}" does not exist to be deleted.')
            except Exception as e:
                await db.session.rollback()
                raise e