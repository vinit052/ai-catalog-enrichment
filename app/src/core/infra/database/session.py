from sqlalchemy.orm import sessionmaker

from core.infra.database.connection import engine


SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()