#pylint:disable=C0103,W0718
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from src.infra.db.sql.config.connection.sqlite_connection_string import SQLiteConnectionString

def clear_database(database_url: str) -> None:
    """
    Remove todos os dados de todas as tabelas do banco de dados.

    :param database_url: URL de conexão com o banco de dados (ex.: 'sqlite:///example.db')
    """
    engine = create_engine(database_url)
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        meta = MetaData()
        meta.reflect(bind=engine)  # Obtém todas as tabelas do banco
        
        for table in reversed(meta.sorted_tables):  # Garante que a ordem respeita chaves estrangeiras
            session.execute(table.delete())  # Remove todos os registros da tabela

        session.commit()  # Confirma as exclusões
        print("Todas as tabelas foram limpas com sucesso.")
    
    except Exception as e:
        session.rollback()
        print(f"Erro ao limpar o banco de dados: {e}")
    
    finally:
        session.close()

def setUP() -> None:
    '''
    clean database SQLiteConnectionString
    '''
    database_url = SQLiteConnectionString.get_sync_connection_string()
    clear_database(database_url)