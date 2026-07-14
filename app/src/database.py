from sqlalchemy import create_engine

from config import settings



engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True
)


def get_database():

    connection = engine.connect()

    try:

        yield connection

    finally:

        connection.close()