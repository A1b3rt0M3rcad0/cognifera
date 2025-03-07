from src.infra.db.sql.test.utils.setUP import setUP
from src.infra.db.sql.repositories.async_user_repository import AsyncUserRepository
from src.infra.db.sql.connection_handler.async_db_connection_handler import AsyncDBConnectionHandler
from src.infra.db.sql.config.connection.sqlite_connection_string import SQLiteConnectionString
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime, timezone
import pytest

@pytest.mark.asyncio
async def test_async_user_repository_insert() -> None:
    setUP()

    mocked_email = 'test_async_user_repository_insert@gmail.com'
    mocked_username = 'mocked_username'
    mocked_password = 'mocked_password'
    mocked_flash_card_generated_in_the_month = 10

    async_db_connection_handler = AsyncDBConnectionHandler(SQLiteConnectionString)
    async_user_repository = AsyncUserRepository(async_db_connection_handler)

    await async_user_repository.insert(
        email=mocked_email,
        username=mocked_username,
        password=mocked_password,
        flash_card_generated_in_the_month=mocked_flash_card_generated_in_the_month
    )

    async with AsyncSession(bind=async_db_connection_handler.get_engine()) as session:
        result = await session.execute(
            text("SELECT * FROM user WHERE email = :email"), {"email": mocked_email}
        )
        user_list = result.all()
    
    assert user_list[0].email == mocked_email
    assert user_list[0].username == mocked_username
    assert user_list[0].password == mocked_password
    assert user_list[0].flash_card_generated_in_the_month == mocked_flash_card_generated_in_the_month

@pytest.mark.asyncio
async def test_async_user_repository_delete() -> None:
    setUP()

    mocked_email = 'test_async_user_repository_delete@gmail.com'
    mocked_username = 'mocked_username'
    mocked_password = 'mocked_password'
    mocked_flash_card_generated_in_the_month = 10
    mocked_created_at = datetime.now(timezone.utc)

    async_db_connection_handler = AsyncDBConnectionHandler(SQLiteConnectionString)

    async with AsyncSession(bind=async_db_connection_handler.get_engine()) as session:
        await session.execute(
            text("""
                INSERT INTO user (email, username, password, flash_card_generated_in_the_month, created_at)
                VALUES (:email, :username, :password, :flash_card_generated_in_the_month, :created_at)
            """),
            {
                "email": mocked_email,
                "username": mocked_username,
                "password": mocked_password,
                "flash_card_generated_in_the_month": mocked_flash_card_generated_in_the_month,
                "created_at": mocked_created_at
            }
        )
        await session.commit()

    async_user_repository = AsyncUserRepository(async_db_connection_handler)
    await async_user_repository.delete(mocked_email)

    async with AsyncSession(bind=async_db_connection_handler.get_engine()) as session:
        result = await session.execute(
            text("SELECT * FROM user WHERE email = :email"), {"email": mocked_email}
        )
        user_list = result.all()

    assert len(user_list) == 0

@pytest.mark.asyncio
async def test_async_user_repository_select() -> None:
    setUP()

    mocked_email = 'test_async_user_repository_select@gmail.com'
    mocked_username = 'mocked_username'
    mocked_password = 'mocked_password'
    mocked_flash_card_generated_in_the_month = 10
    mocked_created_at = datetime.now(timezone.utc)

    async_db_connection_handler = AsyncDBConnectionHandler(SQLiteConnectionString)

    async with AsyncSession(bind=async_db_connection_handler.get_engine()) as session:
        await session.execute(
            text("""
                INSERT INTO user (email, username, password, flash_card_generated_in_the_month, created_at)
                VALUES (:email, :username, :password, :flash_card_generated_in_the_month, :created_at)
            """),
            {
                "email": mocked_email,
                "username": mocked_username,
                "password": mocked_password,
                "flash_card_generated_in_the_month": mocked_flash_card_generated_in_the_month,
                "created_at": mocked_created_at
            }
        )
        await session.commit()

    async_user_repository = AsyncUserRepository(async_db_connection_handler)
    user = await async_user_repository.select(mocked_email)

    assert user.email == mocked_email
    assert user.username == mocked_username
    assert user.password == mocked_password
    assert user.flash_card_generated_in_the_month == mocked_flash_card_generated_in_the_month
    assert user.created_at == mocked_created_at

@pytest.mark.asyncio
async def test_async_user_repository_update() -> None:
    setUP()

    mocked_email = 'test_async_user_repository_select@gmail.com'
    mocked_username = 'mocked_username'
    new_mocked_username = 'new_mocked_username'
    mocked_password = 'mocked_password'
    mocked_flash_card_generated_in_the_month = 10
    mocked_created_at = datetime.now(timezone.utc)

    async_db_connection_handler = AsyncDBConnectionHandler(SQLiteConnectionString)

    async with AsyncSession(bind=async_db_connection_handler.get_engine()) as session:
        await session.execute(
            text("""
                INSERT INTO user (email, username, password, flash_card_generated_in_the_month, created_at)
                VALUES (:email, :username, :password, :flash_card_generated_in_the_month, :created_at)
            """),
            {
                "email": mocked_email,
                "username": mocked_username,
                "password": mocked_password,
                "flash_card_generated_in_the_month": mocked_flash_card_generated_in_the_month,
                "created_at": mocked_created_at
            }
        )
        await session.commit()

    update_params = {"username": new_mocked_username}
    async_user_repository = AsyncUserRepository(async_db_connection_handler)
    await async_user_repository.update(mocked_email, update_params)

    async with AsyncSession(bind=async_db_connection_handler.get_engine()) as session:
        result = await session.execute(
            text("SELECT * FROM user WHERE email = :email"), {"email": mocked_email}
        )
        user_list = result.all()

    assert user_list[0].username == new_mocked_username