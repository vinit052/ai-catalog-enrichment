import os
from dotenv import load_dotenv
load_dotenv()


class AppSettings:
    NAME = os.getenv("APP_NAME", "my-app")
    ENV = os.getenv("APP_ENV", "development")
    DEBUG = ENV == "development"


class DatabaseSettings:
    URL = os.getenv("DATABASE_URL")


class RedisSettings:
    URL = os.getenv("REDIS_URL")


class QdrantSettings:
    URL = os.getenv("QDRANT_URL")
    API_KEY = os.getenv("QDRANT_API_KEY")


class LLMSettings:
    PROVIDER = os.getenv("LLM_PROVIDER", "openai")

    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")


class HTTPSettings:
    TIMEOUT = int(os.getenv("HTTP_TIMEOUT", "30"))


class Settings:
    app = AppSettings()
    database = DatabaseSettings()
    redis = RedisSettings()
    qdrant = QdrantSettings()
    llm = LLMSettings()
    http = HTTPSettings()


settings = Settings()