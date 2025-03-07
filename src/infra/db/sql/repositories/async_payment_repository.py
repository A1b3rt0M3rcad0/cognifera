from sqlalchemy.future import select
from sqlalchemy import update, delete
from src.infra.db.sql.interfaces.i_async_db_connection_handler import IAsyncDBConnectionHandler
from src.data.interfaces.i_async_payment_repository import IAsyncPaymentRepository
from src.domain.models.payment import Payment
from src.infra.db.sql.entities.payment import Payment as PaymentEntity
from typing import Dict, List
from datetime import datetime

class AsyncPaymentRepository(IAsyncPaymentRepository):

    def __init__(self, db_connection_handler: IAsyncDBConnectionHandler) -> None:
        self.__db_connection_handler = db_connection_handler
    
    async def insert(
        self,
        user_email: str,
        plan_name: str,
        amount: float,
        payment_channel: str,
        transaction_id: str,
        currency: str,
        payment_method_details: str,
        failure_reason: str,
        payment_gateway: str,
        payment_date: datetime,
    ) -> None:
        async with self.__db_connection_handler as db:
            try:
                payment = PaymentEntity(
                    user_email=user_email,
                    plan_name=plan_name,
                    amount=amount,
                    payment_channel=payment_channel,
                    transaction_id=transaction_id,
                    currency=currency,
                    payment_method_details=payment_method_details, 
                    failure_reason=failure_reason,
                    payment_gateway=payment_gateway,
                    payment_date=payment_date,
                )
                db.session.add(payment)
                await db.session.commit()
            except Exception as e:
                await db.session.rollback()
                raise e
    
    async def select(self, select_params: Dict) -> List[Payment]:
        async with self.__db_connection_handler as db:
            try:
                stmt = select(PaymentEntity).filter_by(**select_params)
                result = await db.session.execute(stmt)
                payments = result.scalars().all()
                return payments
            except Exception as e:
                await db.session.rollback()
                raise e
    
    async def update(self, select_params: Dict, update_params: Dict) -> None:
        async with self.__db_connection_handler as db:
            try:
                stmt = update(PaymentEntity).filter_by(**select_params).values(**update_params)
                await db.session.execute(stmt)
                await db.session.commit()
            except Exception as e:
                await db.session.rollback()
                raise e
    
    async def delete(self, payment_params: Dict) -> None:
        async with self.__db_connection_handler as db:
            try:
                stmt = delete(PaymentEntity).filter_by(**payment_params)
                await db.session.execute(stmt)
                await db.session.commit()
            except Exception as e:
                await db.session.rollback()
                raise e