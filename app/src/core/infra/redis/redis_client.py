import redis
from core.config import settings

redis_client = redis.from_url(
    settings.redis.URL,
    decode_responses=True,
    socket_timeout=None,
    socket_connect_timeout=5,
)

def get_redis():
    return redis_client