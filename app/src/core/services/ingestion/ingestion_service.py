from core.services.ingestion.parser_service import ParserService
from core.services.ingestion.validation_service import ValidationService
from core.services.ingestion.enrichment_queue_service import EnrichmentQueueService
from core.services.ingestion.response_builder import ResponseBuilder
from core.mappers.import_mapper import create_import_model


class IngestionService:

    def __init__(
        self,
        import_service,
        parser_service: ParserService,
        validation_service: ValidationService,
        queue_service: EnrichmentQueueService,
    ):
        self.import_service = import_service
        self.parser_service = parser_service
        self.validation_service = validation_service
        self.queue_service = queue_service


    async def ingest(self, file):

        records = await self.parser_service.parse(file)

        validation = (
            self.validation_service
            .validate(records)
        )

        import_model = create_import_model(
            filename=file.filename,
            total_records=len(records),
            valid_records=len(validation.valid_records),
            invalid_records=len(validation.invalid_records),
        )

        saved_import, saved_items = (
            self.import_service
            .create_import_with_items(
                import_record=import_model,
                valid_records=validation.valid_records,
            )
        )

        self.queue_service.publish_items(
            saved_import,
            saved_items,
        )

        return ResponseBuilder.success(
            import_id=saved_import.id,
            filename=file.filename,
            validation=validation,
        )