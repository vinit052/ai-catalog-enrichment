import json
from core.infra.redis.redis_client import redis_client

QUEUE_NAME = "item_enrichment_queue"

class RedisPublisher:

    @staticmethod
    def publish(item):
        redis_client.rpush(
            QUEUE_NAME,
            json.dumps(item),
        )