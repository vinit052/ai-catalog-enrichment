from core.repositories.base_repository import BaseRepository
from core.infra.database.models.import_model import Import

from core.exceptions.database import (
    RecordNotFoundException
)


class ImportRepository(BaseRepository):

    def create(
        self,
        import_record: Import
    ):
        self.db.add(import_record)
        self.db.flush()          # Generates ID without committing
        self.db.refresh(import_record)

        return import_record

    def get_by_id(
        self,
        import_id: str
    ):
        record = (
            self.db.query(Import)
            .filter(Import.id == import_id)
            .first()
        )

        if not record:
            raise RecordNotFoundException(
                f"Import {import_id} not found"
            )

        return record

    def update_status(
        self,
        import_id: str,
        status: str
    ):
        record = self.get_by_id(import_id)

        record.status = status

        return record