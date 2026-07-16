from core.repositories.item_repository import ItemRepository
from core.infra.database.models.item import Item


class ItemService:

    def __init__(
        self,
        item_repository: ItemRepository
    ):
        self.item_repository = item_repository

    def create_bulk(
        self,
        items: list[Item]
    ):
        return self.item_repository.create_bulk(items)

    def get_pending_items(
        self,
        limit: int = 100
    ):
        return self.item_repository.get_pending_items(limit)

    def update_enrichment(
        self,
        item_id: int,
        enrich_data: dict
    ):
        item = self.item_repository.update_enrichment(
            item_id=item_id,
            enrich_data=enrich_data,
        )

        self.item_repository.db.commit()

        return item