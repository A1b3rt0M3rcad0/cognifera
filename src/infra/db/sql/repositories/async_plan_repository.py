from sqlalchemy.future import select
from sqlalchemy import update
from src.infra.db.sql.interfaces.i_async_db_connection_handler import IAsyncDBConnectionHandler
from src.data.interfaces.i_async_plan_repository import IAsyncPlanRepository
from src.domain.models.plan import Plan
from src.infra.db.sql.entities.plan import Plan as PlanEntity
from typing import Dict

class AsyncPlanRepository(IAsyncPlanRepository):

    def __init__(self, db_connection_handler: IAsyncDBConnectionHandler) -> None:
        self.__db_connection_handler = db_connection_handler
    
    async def insert(self, name:str, price:float, flash_card_limit_per_month:int, days:int) -> None:
        async with self.__db_connection_handler as db:
            try:
                plan = PlanEntity(name=name, 
                                  price=price, 
                                  flash_card_limit_per_month=flash_card_limit_per_month, 
                                  days=days)
                db.session.add(plan)
                await db.session.commit()
            except Exception as e:
                await db.session.rollback()
                raise e
    
    async def select(self, name:str) -> Plan:
        async with self.__db_connection_handler as db:
            try:
                stmt = select(PlanEntity).where(PlanEntity.name == name)
                result = await db.session.execute(stmt)
                plan = result.scalars().all()
                return plan[0]
            except Exception as e:
                await db.rollback()
                raise e
    
    async def update(self, name:str, update_params:Dict) -> None:
        async with self.__db_connection_handler as db:
            try:
                stmt = update(PlanEntity).where(PlanEntity.name == name).values(update_params)
                await db.session.execute(stmt)
                await db.session.commit()
            except Exception as e:
                await db.session.rollback()
                raise e
    
    async def delete(self, name:str) -> None:
        async with self.__db_connection_handler as db:
            try:
                stmt = select(PlanEntity).where(PlanEntity.name == name)
                result = await db.session.execute(stmt)
                plan = result.scalar_one_or_none()
                if plan:
                    await db.session.delete(plan)
                    await db.session.commit()
                else:
                    raise RuntimeError(f'The plan with name "{name}" does not exist to be deleted.')
            except Exception as e:
                await db.session.rollback()
                raise e