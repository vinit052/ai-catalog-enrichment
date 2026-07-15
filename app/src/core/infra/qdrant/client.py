from qdrant_client import QdrantClient
from core.config import settings

qdrant_client = QdrantClient(
    url=settings.qdrant.URL,
    api_key=settings.qdrant.API_KEY,
)


def get_qdrant():
    return qdrant_client