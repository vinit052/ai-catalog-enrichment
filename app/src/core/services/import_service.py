from core.mappers.item_mapper import create_item_models
from sqlalchemy.orm import Session

from core.repositories.import_repository import ImportRepository
from core.repositories.item_repository import ItemRepository

from core.infra.database.models.import_model import Import
from core.infra.database.models.item import Item


class ImportService:

    def __init__(
        self,
        db: Session,
        import_repository: ImportRepository,
        item_repository: ItemRepository,
    ):
        self.db = db
        self.import_repository = import_repository
        self.item_repository = item_repository

    def create(
        self,
        import_record: Import
    ):
        try:
            saved_import = self.import_repository.create(import_record)

            self.db.commit()
            self.db.refresh(saved_import)

            return saved_import

        except Exception:
            self.db.rollback()
            raise


    def create_import_with_items(
        self,
        import_record,
        valid_records,
    ):
        try:

            saved_import = (
                self.import_repository
                .create(import_record)
            )


            items = create_item_models(
                import_id=saved_import.id,
                valid_records=valid_records,
            )


            self.item_repository.create_bulk(
                items
            )


            self.db.commit()

            self.db.refresh(
                saved_import
            )

            return saved_import


        except Exception:
            self.db.rollback()
            raise

    def get_by_id(
        self,
        import_id: str
    ):
        return self.import_repository.get_by_id(import_id)

    def update_status(
        self,
        import_id: str,
        status: str
    ):
        try:
            record = self.import_repository.update_status(
                import_id=import_id,
                status=status,
            )

            self.db.commit()
            return record
        except Exception:
            self.db.rollback()
            raise