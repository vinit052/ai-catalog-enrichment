from sqlalchemy import create_engine

from core.config import settings

engine = create_engine(
    settings.database.URL,
    pool_pre_ping=True,
)