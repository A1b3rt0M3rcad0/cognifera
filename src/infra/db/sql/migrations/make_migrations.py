#pylint:disable=W0401,W0611
from src.infra.db.sql.config.base_entity.base import Base
from src.infra.db.sql.entities.payment import Payment
from src.infra.db.sql.entities.plan import Plan
from src.infra.db.sql.entities.subscription import Subscription
from src.infra.db.sql.entities.usage_stats import UsageStats
from src.infra.db.sql.entities.user import User
from src.infra.db.sql.config.interfaces.i_database_connection_string import IDatabaseConnectionString
from src.infra.db.sql.connection_handler.db_connection_handler import DBConnectionHandler

class Migrations:

    @staticmethod
    def make_migrations(connection_string:IDatabaseConnectionString) -> None:
        db_connection_handler = DBConnectionHandler(connection_string)
        engine = db_connection_handler.get_engine()
        Base.metadata.create_all(engine)