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

@pytest.mark.asyncio
async def test_async_user_repository_delete() -> None:

    setUP()

    mocked_email = 'test_async_user_repository_delete@gmail.com'
    mocked_username = 'mocked_username'
    mocked_password = 'mocked_password'
    mocked_flash_card_generated_in_the_month = 10
    mocked_created_at = datetime.now(timezone.utc)

    async_db_connection_handler = AsyncDBConnectionHandler(SQLiteConnectionString)
    async_engine = async_db_connection_handler.get_engine()
    async_session = AsyncSession(bind=async_engine)

    await async_session.execute(
        text(f"""
            INSERT INTO user (email, username, password, flash_card_generated_in_the_month, created_at)
            VALUES ("{mocked_email}", "{mocked_username}", "{mocked_password}", {mocked_flash_card_generated_in_the_month}, "{mocked_created_at}")
        """
        )
    )

    await async_session.commit()
    
    async_user_repository = AsyncUserRepository(async_db_connection_handler)
    await async_user_repository.delete(mocked_email)

    result = await async_session.execute(
        text(f"""
            SELECT * FROM user WHERE email = "{mocked_email}"
        """
        )
    )

    user_list = result.all()
    await async_session.close()

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
    async_engine = async_db_connection_handler.get_engine()
    async_session = AsyncSession(bind=async_engine)

    await async_session.execute(
        text(f"""
            INSERT INTO user (email, username, password, flash_card_generated_in_the_month, created_at)
            VALUES ("{mocked_email}", "{mocked_username}", "{mocked_password}", {mocked_flash_card_generated_in_the_month}, "{mocked_created_at}")
        """
        )
    )

    await async_session.commit()
    
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
    async_engine = async_db_connection_handler.get_engine()
    async_session = AsyncSession(bind=async_engine)

    await async_session.execute(
        text(f"""
            INSERT INTO user (email, username, password, flash_card_generated_in_the_month, created_at)
            VALUES ("{mocked_email}", "{mocked_username}", "{mocked_password}", {mocked_flash_card_generated_in_the_month}, "{mocked_created_at}")
        """
        )
    )

    await async_session.commit()

    update_params = {
        "username": new_mocked_username
    }

    async_user_repository = AsyncUserRepository(async_db_connection_handler)
    await async_user_repository.update(mocked_email, update_params)

    result = await async_session.execute(
        text(f"""
            SELECT * FROM user WHERE email = "{mocked_email}"
        """
        )
    )
    await async_session.close()

    user_list = result.all()


    assert user_list[0].username == new_mocked_username
