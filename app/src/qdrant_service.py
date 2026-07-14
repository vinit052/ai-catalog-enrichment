from qdrant_client import QdrantClient

from config import settings


qdrant = QdrantClient(
    url=settings.QDRANT_URL,
    api_key=settings.QDRANT_API_KEY
)


def get_qdrant():
    return qdrant