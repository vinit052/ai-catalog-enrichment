import json

from core.infra.redis.redis_client import redis_client

##print(redis_client.connection_pool.connection_kwargs)

QUEUE_NAME = "item_enrichment_queue"


def start_consumer():

    print("Consumer started..........")

    while True:

        result = redis_client.blpop(
            QUEUE_NAME
        )

        _, message = result

        data = json.loads(message)

        print("=" * 50)
        print("Message received")
        print(data)
        print("=" * 50)


if __name__ == "__main__":
    start_consumer()