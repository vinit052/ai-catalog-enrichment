from core.repositories.base_repository import BaseRepository
from core.infra.database.models.item import Item


class ItemRepository(BaseRepository):

    def create_bulk(
        self,
        items: list[Item]
    ):
        self.db.add_all(items)
        self.db.flush()
        return items

    def get_pending_items(
        self,
        limit: int = 100
    ):
        return (
            self.db.query(Item)
            .filter(Item.status == "PENDING")
            .limit(limit)
            .all()
        )

    def update_enrichment(
        self,
        item_id: int,
        enrich_data: dict
    ):
        item = (
            self.db.query(Item)
            .filter(Item.id == item_id)
            .first()
        )

        if item:
            item.enrich_data = enrich_data
            item.status = "REVIEW_PENDING"

        return item