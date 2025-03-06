#pylint:disable=W0401,W0611
from src.infra.db.sql.config.base_entity.base import Base
from src.infra.db.sql.entities.payment import Payment
from src.infra.db.sql.entities.plan import Plan
from src.infra.db.sql.entities.subscription import Subscription
from src.infra.db.sql.entities.usage_stats import UsageStats
from src.infra.db.sql.entities.user import User
from src.infra.db.sql.config.interfaces.i_database_connection_string import IDatabaseConnectionString
from sqlalchemy import create_engine

class Migrations:

    @staticmethod
    def make_migrations(connection_string:IDatabaseConnectionString) -> None:
        sync_engine = create_engine(connection_string.get_sync_connection_string())
        Base.metadata.create_all(sync_engine)