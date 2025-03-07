from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
from src.infra.db.sql.test.utils.setUP import setUP
from src.infra.db.sql.config.connection.sqlite_connection_string import SQLiteConnectionString
from src.infra.db.sql.connection_handler.async_db_connection_handler import AsyncDBConnectionHandler
from src.infra.db.sql.repositories.async_plan_repository import AsyncPlanRepository
from datetime import datetime, timezone
import pytest

@pytest.mark.asyncio
async def test_async_plan_repository_insert() -> None:
    setUP()

    mocked_name = 'mocked_name'
    mocked_price = 9.99
    mocked_flash_card_limit_per_month = 10
    mocked_days = 30

    async_db_connection_handler = AsyncDBConnectionHandler(SQLiteConnectionString)
    async_plan_repository = AsyncPlanRepository(async_db_connection_handler)

    await async_plan_repository.insert(
        name=mocked_name,
        price=mocked_price,
        flash_card_limit_per_month=mocked_flash_card_limit_per_month,
        days=mocked_days
    )

    async with AsyncSession(bind=async_db_connection_handler.get_engine()) as session:
        result = await session.execute(
            text("SELECT * FROM plan WHERE name = :name"),
            {"name": mocked_name}
        )
        plan = result.one_or_none()

    assert plan
    assert plan.name == mocked_name
    assert plan.price == mocked_price
    assert plan.flash_card_limit_per_month == mocked_flash_card_limit_per_month
    assert plan.days == mocked_days


@pytest.mark.asyncio
async def test_async_plan_repository_select() -> None:
    setUP()

    mocked_name = 'mocked_name'
    mocked_price = 9.99
    mocked_flash_card_limit_per_month = 10
    mocked_days = 30
    mocked_created_at = datetime.now(timezone.utc)

    async_db_connection_handler = AsyncDBConnectionHandler(SQLiteConnectionString)

    async with AsyncSession(bind=async_db_connection_handler.get_engine()) as session:
        await session.execute(
            text("""
                INSERT INTO plan (name, price, flash_card_limit_per_month, days, created_at)
                VALUES (:name, :price, :flash_card_limit_per_month, :days, :created_at)
            """),
            {
                "name": mocked_name,
                "price": mocked_price,
                "flash_card_limit_per_month": mocked_flash_card_limit_per_month,
                "days": mocked_days,
                "created_at": mocked_created_at
            }
        )
        await session.commit()

    async_plan_repository = AsyncPlanRepository(async_db_connection_handler)
    plan = await async_plan_repository.select(mocked_name)

    assert plan.name == mocked_name
    assert plan.price == mocked_price
    assert plan.flash_card_limit_per_month == mocked_flash_card_limit_per_month
    assert plan.days == mocked_days
    assert plan.created_at == mocked_created_at

@pytest.mark.asyncio
async def test_async_plan_repository_update() -> None:
    setUP()

    mocked_name = 'mocked_name'
    new_mocked_name = 'new_mocked_name'
    mocked_price = 9.99
    mocked_flash_card_limit_per_month = 10
    mocked_days = 30
    mocked_created_at = datetime.now(timezone.utc)

    async_db_connection_handler = AsyncDBConnectionHandler(SQLiteConnectionString)

    async with AsyncSession(bind=async_db_connection_handler.get_engine()) as session:
        await session.execute(
            text("""
                INSERT INTO plan (name, price, flash_card_limit_per_month, days, created_at)
                VALUES (:name, :price, :flash_card_limit_per_month, :days, :created_at)
            """),
            {
                "name": mocked_name,
                "price": mocked_price,
                "flash_card_limit_per_month": mocked_flash_card_limit_per_month,
                "days": mocked_days,
                "created_at": mocked_created_at
            }
        )
        await session.commit()
    
    async_plan_repository = AsyncPlanRepository(async_db_connection_handler)
    await async_plan_repository.update(
        name=mocked_name,
        update_params={
            'name': new_mocked_name
        }
    )

    async with AsyncSession(bind=async_db_connection_handler.get_engine()) as session:

        result = await session.execute(
            text("""
                SELECT * FROM plan WHERE name = :name
            """),
            {
                "name": new_mocked_name
            }
        )

    plan = result.one_or_none()

    assert plan.name == new_mocked_name

@pytest.mark.asyncio
async def test_async_plan_repository_delete() -> None:
    setUP()

    mocked_name = 'mocked_name'
    mocked_price = 9.99
    mocked_flash_card_limit_per_month = 10
    mocked_days = 30
    mocked_created_at = datetime.now(timezone.utc)

    async_db_connection_handler = AsyncDBConnectionHandler(SQLiteConnectionString)

    async with AsyncSession(bind=async_db_connection_handler.get_engine()) as session:
        await session.execute(
            text("""
                INSERT INTO plan (name, price, flash_card_limit_per_month, days, created_at)
                VALUES (:name, :price, :flash_card_limit_per_month, :days, :created_at)
            """),
            {
                "name": mocked_name,
                "price": mocked_price,
                "flash_card_limit_per_month": mocked_flash_card_limit_per_month,
                "days": mocked_days,
                "created_at": mocked_created_at
            }
        )
        await session.commit()

    async_plan_repository = AsyncPlanRepository(async_db_connection_handler)
    await async_plan_repository.delete(mocked_name)

    async with AsyncSession(bind=async_db_connection_handler.get_engine()) as session:

        result = await session.execute(
            text("""
                SELECT * FROM plan WHERE name = :name
            """),
            {
                "name": mocked_name
            }
        )

    plan = result.one_or_none()

    assert not plan