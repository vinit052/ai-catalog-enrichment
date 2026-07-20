from fastapi import Depends
from sqlalchemy.orm import Session
from dependencies.database import get_db
from core.repositories.import_repository import ImportRepository
from core.repositories.item_repository import ItemRepository
from core.services.import_service import ImportService
from core.services.ingestion.ingestion_service import IngestionService
from core.services.ingestion.parser_service import ParserService
from core.services.ingestion.validation_service import ValidationService
from core.services.ingestion.enrichment_queue_service import EnrichmentQueueService


def get_ingestion_service(
    db: Session = Depends(get_db),
) -> IngestionService:

    import_repository = ImportRepository(db)
    item_repository = ItemRepository(db)
    import_service = ImportService(
        db=db,
        import_repository=import_repository,
        item_repository=item_repository,
    )

    return IngestionService(
        import_service=import_service,
        parser_service=ParserService(),
        validation_service=ValidationService(),
        queue_service=EnrichmentQueueService(),
    )