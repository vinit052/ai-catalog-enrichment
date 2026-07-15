from fastapi import APIRouter

from core.infra.redis.redis_client import get_redis
from core.infra.qdrant.client import get_qdrant


router = APIRouter()


@router.get(
    "/",
    summary="Check application health",
    description="""
Checks connectivity to all backend services.

Services checked:
- Redis
- Qdrant

Returns the status of each dependency.
""",
)
def health():

    redis = get_redis()
    qdrant = get_qdrant()

    redis_status = False
    qdrant_status = False

    try:
        redis.ping()
        redis_status = True
    except Exception:
        pass

    try:
        qdrant.get_collections()
        qdrant_status = True
    except Exception:
        pass

    return {
        "status": "ok",
        "services": {
            "redis": redis_status,
            "qdrant": qdrant_status,
        },
    }