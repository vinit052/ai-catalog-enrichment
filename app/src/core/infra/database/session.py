from .connection import engine


def get_database():
    connection = engine.connect()

    try:
        yield connection
    finally:
        connection.close()