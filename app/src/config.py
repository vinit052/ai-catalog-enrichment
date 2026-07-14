import os
from dotenv import load_dotenv

load_dotenv()


class Settings:

    APP_ENV = os.getenv(
        "APP_ENV",
        "development"
    )

    DATABASE_URL = os.getenv(
        "DATABASE_URL"
    )

    REDIS_URL = os.getenv(
        "REDIS_URL"
    )

    QDRANT_URL = os.getenv(
        "QDRANT_URL"
    )

    QDRANT_API_KEY = os.getenv(
        "QDRANT_API_KEY"
    )


settings = Settings()