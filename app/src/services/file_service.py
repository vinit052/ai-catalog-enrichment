from core.infra.redis.publisher import RedisPublisher
from core.mappers.import_mapper import (
    create_import_model,
)

from core.mappers.item_mapper import (
    create_item_models,
)

from parsers.csv_parser import CSVParser
from parsers.excel_parser import ExcelParser
from parsers.image_parser import ImageParser

from validators.product_import_validator import (
    ProductImportValidator,
    ValidationStatus,
)


PARSERS = {
    "csv": CSVParser(),
    "xls": ExcelParser(),
    "xlsx": ExcelParser(),
    "jpg": ImageParser(),
    "jpeg": ImageParser(),
    "png": ImageParser(),
}


async def process_file(
    file,
    import_service,
):

    extension = (
        file.filename
        .split(".")[-1]
        .lower()
    )


    parser = PARSERS.get(extension)

    if not parser:
        raise ValueError(
            "Unsupported file format"
        )


    # Parse uploaded file
    records = await parser.parse(file)


    # Validate records
    validation_result = (
        ProductImportValidator()
        .validate(
            None,
            records,
        )
    )


    valid_records = []
    invalid_records = []


    for row in validation_result["rows"]:

        if row["status"] == ValidationStatus.VALID:

            valid_records.append(
                row["data"]
            )


        else:

            invalid_records.append(
                {
                    "row": row["row"],
                    "data": row["data"],
                    "errors": (
                        row.get("errors", [])
                        +
                        row.get("warnings", [])
                    ),
                }
            )


    # Create Import model
    import_model = create_import_model(
        filename=file.filename,
        total_records=len(records),
        valid_records=len(valid_records),
        invalid_records=len(invalid_records),
    )


    # Save import + items in one transaction
    saved_import, saved_items = (
        import_service
        .create_import_with_items(
            import_record=import_model,
            valid_records=valid_records,
        )
    )

    # Publish each item to Redis for further processing
    for item in saved_items:
        RedisPublisher.publish(
            {
                "item_id": item.id,
                "import_id": saved_import.id,
            }
        )

    error_file = None

    if invalid_records:

        # Later replace with ErrorReportService
        error_file = (
            f"/imports/{saved_import.id}/errors.xlsx"
        )


    return {
        "import_id": saved_import.id,
        "filename": file.filename,

        "summary": {
            "total_records": len(records),
            "valid_records": len(valid_records),
            "invalid_records": len(invalid_records),
        },

        "processing": {
            "valid_records_stored": True,
            "enrichment_status": "PENDING",
        },

        "error_report": {
            "available": bool(error_file),
            "file": error_file,
        },
    }