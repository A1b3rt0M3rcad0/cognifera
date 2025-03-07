#pylint:disable=C0412
from src.infra.db.sql.test.utils.setUP import setUP
from src.infra.db.sql.repositories.async_payment_repository import AsyncPaymentRepository
from src.infra.db.sql.connection_handler.async_db_connection_handler import AsyncDBConnectionHandler
from src.infra.db.sql.config.connection.sqlite_connection_string import SQLiteConnectionString
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime, timezone
import pytest
from src.domain.status.payment_status import Status
from src.domain.status.payment_refund_status import RefundStatus

@pytest.mark.asyncio
async def test_async_payment_repository_insert() -> None:
    setUP()

    mocked_user_email = 'test_async_payment_repository_insert@gmail.com'
    mocked_plan_name = 'test_plan'
    mocked_amount = 9.99
    mocked_payment_channel = 'credit_card'
    mocked_transaction_id = 'txn_123456'
    mocked_currency = 'USD'
    mocked_payment_method_details = 'VISA ****1234'
    mocked_failure_reason = ''
    mocked_payment_gateway = 'stripe'
    mocked_payment_date = datetime.now(timezone.utc)

    async_db_connection_handler = AsyncDBConnectionHandler(SQLiteConnectionString)
    async_payment_repository = AsyncPaymentRepository(async_db_connection_handler)

    await async_payment_repository.insert(
        user_email=mocked_user_email,
        plan_name=mocked_plan_name,
        amount=mocked_amount,
        payment_channel=mocked_payment_channel,
        transaction_id=mocked_transaction_id,
        currency=mocked_currency,
        payment_method_details=mocked_payment_method_details,
        failure_reason=mocked_failure_reason,
        payment_gateway=mocked_payment_gateway,
        payment_date=mocked_payment_date
    )

    async with AsyncSession(bind=async_db_connection_handler.get_engine()) as session:
        result = await session.execute(
            text("SELECT * FROM payment WHERE user_email = :user_email"),
            {"user_email": mocked_user_email}
        )
        payment = result.one_or_none()

    assert payment
    assert payment.user_email == mocked_user_email
    assert payment.plan_name == mocked_plan_name
    assert payment.amount == mocked_amount
    assert payment.payment_channel == mocked_payment_channel
    assert payment.transaction_id == mocked_transaction_id
    assert payment.currency == mocked_currency
    assert payment.payment_method_details == mocked_payment_method_details
    assert payment.failure_reason == mocked_failure_reason
    assert payment.payment_gateway == mocked_payment_gateway

@pytest.mark.asyncio
async def test_async_payment_repository_select() -> None:
    setUP()

    mocked_user_email = 'test_async_payment_repository_select@gmail.com'
    mocked_plan_name = 'test_plan'
    mocked_amount = 9.99
    mocked_payment_channel = 'credit_card'
    mocked_transaction_id = 'txn_123456'
    mocked_currency = 'USD'
    mocked_payment_method_details = 'VISA ****1234'
    mocked_failure_reason = ''
    mocked_payment_gateway = 'stripe'
    mocked_payment_date = datetime.now(timezone.utc)
    mocked_payment_status = Status.FINISHED.value
    mocked_refund_status = RefundStatus.NOT_REFUNDED.value
    mocked_created_at = datetime.now(timezone.utc)

    async_db_connection_handler = AsyncDBConnectionHandler(SQLiteConnectionString)

    async with AsyncSession(bind=async_db_connection_handler.get_engine()) as session:
        await session.execute(
            text("""INSERT INTO payment (user_email, 
            plan_name, amount, 
            payment_channel, 
            transaction_id, 
            currency, 
            payment_method_details, 
            failure_reason, 
            payment_gateway, 
            payment_date,
            status,
            refund_status,
            created_at) 
            VALUES (:user_email, 
            :plan_name, 
            :amount, 
            :payment_channel, 
            :transaction_id, 
            :currency, 
            :payment_method_details, 
            :failure_reason, 
            :payment_gateway, 
            :payment_date,
            :status,
            :refund_status,
            :created_at)"""),
            {
                "user_email": mocked_user_email,
                "plan_name": mocked_plan_name,
                "amount": mocked_amount,
                "payment_channel": mocked_payment_channel,
                "transaction_id": mocked_transaction_id,
                "currency": mocked_currency,
                "payment_method_details": mocked_payment_method_details,
                "failure_reason": mocked_failure_reason,
                "payment_gateway": mocked_payment_gateway,
                "payment_date": mocked_payment_date,
                "status": mocked_payment_status,
                "refund_status": mocked_refund_status,
                "created_at": mocked_created_at
                }
        )
        await session.commit()
    
    async_payment_repository = AsyncPaymentRepository(async_db_connection_handler)

    select_params = {
        'user_email': mocked_user_email,
        'plan_name': mocked_plan_name,
    }

    list_payment = await async_payment_repository.select(select_params)

    assert list_payment
    assert list_payment[0].user_email == mocked_user_email
    assert list_payment[0].plan_name == mocked_plan_name
    assert list_payment[0].amount == mocked_amount
    assert list_payment[0].payment_channel == mocked_payment_channel
    assert list_payment[0].transaction_id == mocked_transaction_id
    assert list_payment[0].currency == mocked_currency
    assert list_payment[0].payment_method_details == mocked_payment_method_details
    assert list_payment[0].failure_reason == mocked_failure_reason
    assert list_payment[0].payment_gateway == mocked_payment_gateway
    assert list_payment[0].payment_date == mocked_payment_date

@pytest.mark.asyncio
async def test_async_payment_repository_update() -> None:
    setUP()

    mocked_user_email = 'test_async_payment_repository_delete@gmail.com'
    mocked_new_user_email = 'test_async_payment_repository_delete@newgmail.com'
    mocked_plan_name = 'test_plan'
    mocked_amount = 9.99
    mocked_payment_channel = 'credit_card'
    mocked_transaction_id = 'txn_123456'
    mocked_currency = 'USD'
    mocked_payment_method_details = 'VISA ****1234'
    mocked_failure_reason = ''
    mocked_payment_gateway = 'stripe'
    mocked_payment_date = datetime.now(timezone.utc)
    mocked_payment_status = Status.FINISHED.value
    mocked_refund_status = RefundStatus.NOT_REFUNDED.value
    mocked_created_at = datetime.now(timezone.utc)

    async_db_connection_handler = AsyncDBConnectionHandler(SQLiteConnectionString)

    async with AsyncSession(bind=async_db_connection_handler.get_engine()) as session:
        result = await session.execute(
            text("""INSERT INTO payment (user_email, 
            plan_name, amount, 
            payment_channel, 
            transaction_id, 
            currency, 
            payment_method_details, 
            failure_reason, 
            payment_gateway, 
            payment_date,
            status,
            refund_status,
            created_at) 
            VALUES (:user_email, 
            :plan_name, 
            :amount, 
            :payment_channel, 
            :transaction_id, 
            :currency, 
            :payment_method_details, 
            :failure_reason, 
            :payment_gateway, 
            :payment_date,
            :status,
            :refund_status,
            :created_at)"""),
            {
                "user_email": mocked_user_email,
                "plan_name": mocked_plan_name,
                "amount": mocked_amount,
                "payment_channel": mocked_payment_channel,
                "transaction_id": mocked_transaction_id,
                "currency": mocked_currency,
                "payment_method_details": mocked_payment_method_details,
                "failure_reason": mocked_failure_reason,
                "payment_gateway": mocked_payment_gateway,
                "payment_date": mocked_payment_date,
                "status": mocked_payment_status,
                "refund_status": mocked_refund_status,
                "created_at": mocked_created_at
                }
        )
        await session.commit()
    

    async_payment_repository = AsyncPaymentRepository(async_db_connection_handler)

    select_params = {
        'user_email': mocked_user_email,
        'plan_name': mocked_plan_name,
    }

    update_prams = {
        'user_email': mocked_new_user_email
    }

    await async_payment_repository.update(select_params, update_prams)

    async with AsyncSession(bind=async_db_connection_handler.get_engine()) as session:
        result = await session.execute(
            text("SELECT * FROM payment WHERE user_email = :user_email"),
            {"user_email": mocked_new_user_email}
        )
        payment = result.one_or_none()
    
    assert payment
    assert payment.user_email == mocked_new_user_email

@pytest.mark.asyncio
async def test_async_payment_repository_delete() -> None:
    setUP()

    mocked_user_email = 'test_async_payment_repository_delete@gmail.com'
    mocked_plan_name = 'test_plan'
    mocked_amount = 9.99
    mocked_payment_channel = 'credit_card'
    mocked_transaction_id = 'txn_123456'
    mocked_currency = 'USD'
    mocked_payment_method_details = 'VISA ****1234'
    mocked_failure_reason = ''
    mocked_payment_gateway = 'stripe'
    mocked_payment_date = datetime.now(timezone.utc)
    mocked_payment_status = Status.FINISHED.value
    mocked_refund_status = RefundStatus.NOT_REFUNDED.value
    mocked_created_at = datetime.now(timezone.utc)

    async_db_connection_handler = AsyncDBConnectionHandler(SQLiteConnectionString)

    async with AsyncSession(bind=async_db_connection_handler.get_engine()) as session:
        await session.execute(
            text("""INSERT INTO payment (user_email, 
            plan_name, amount, 
            payment_channel, 
            transaction_id, 
            currency, 
            payment_method_details, 
            failure_reason, 
            payment_gateway, 
            payment_date,
            status,
            refund_status,
            created_at) 
            VALUES (:user_email, 
            :plan_name, 
            :amount, 
            :payment_channel, 
            :transaction_id, 
            :currency, 
            :payment_method_details, 
            :failure_reason, 
            :payment_gateway, 
            :payment_date,
            :status,
            :refund_status,
            :created_at)"""),
            {
                "user_email": mocked_user_email,
                "plan_name": mocked_plan_name,
                "amount": mocked_amount,
                "payment_channel": mocked_payment_channel,
                "transaction_id": mocked_transaction_id,
                "currency": mocked_currency,
                "payment_method_details": mocked_payment_method_details,
                "failure_reason": mocked_failure_reason,
                "payment_gateway": mocked_payment_gateway,
                "payment_date": mocked_payment_date,
                "status": mocked_payment_status,
                "refund_status": mocked_refund_status,
                "created_at": mocked_created_at
                }
        )
        await session.commit()
    

    async_payment_repository = AsyncPaymentRepository(async_db_connection_handler)

    payment_params = {
        'user_email': mocked_user_email,
        'plan_name': mocked_plan_name,
    }

    await async_payment_repository.delete(payment_params)

    async with AsyncSession(bind=async_db_connection_handler.get_engine()) as session:
        result = await session.execute(
            text("SELECT * FROM payment WHERE user_email = :user_email"),
            {"user_email": mocked_user_email}
        )
        payment = result.one_or_none()

    assert payment is None
