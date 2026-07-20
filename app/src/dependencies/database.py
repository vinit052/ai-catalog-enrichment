from sqlalchemy.orm import Session
from core.infra.database.session import SessionLocal


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()