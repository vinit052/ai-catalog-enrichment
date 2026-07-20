from core.infra.redis.publisher import RedisPublisher

class EnrichmentQueueService:

    def publish_items(
        self,
        saved_import,
        saved_items,
    ):

        for item in saved_items:
            RedisPublisher.publish(
                {
                    "item_id": item.id,
                    "import_id": saved_import.id,
                }
            )