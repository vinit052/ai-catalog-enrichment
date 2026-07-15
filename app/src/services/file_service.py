from parsers.csv_parser import CSVParser
from parsers.excel_parser import ExcelParser
from parsers.image_parser import ImageParser
from validators.product_import_validator import (
    ProductImportValidator,
    ValidationStatus,
)

# Add your repositories/services here later
# from app.src.services.product_service import ProductService
# from app.src.services.error_report_service import ErrorReportService


PARSERS = {
    "csv": CSVParser(),
    "xls": ExcelParser(),
    "xlsx": ExcelParser(),
    "jpg": ImageParser(),
    "jpeg": ImageParser(),
    "png": ImageParser(),
}


async def process_file(file, import_id):

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
    validation_result = ProductImportValidator().validate(
        records
    )

    rows = validation_result["rows"]

    valid_records = []
    invalid_records = []


    for row in rows:

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
                    )
                }
            )


    #
    # Store only valid records
    #
    # await ProductService.bulk_create(
    #     valid_records
    # )


    #
    # Generate error report
    #
    error_file = None

    if invalid_records:

        # error_file = await ErrorReportService.create(
        #     import_id,
        #     invalid_records
        # )

        error_file = (
            f"/imports/{import_id}/errors.xlsx"
        )


    return {
        "import_id": import_id,
        "filename": file.filename,
        "summary": {
            "total_records": len(records),
            "valid_records": len(valid_records),
            "invalid_records": len(invalid_records),
        },
        "processing": {
            "valid_records_stored": True,
            "enrichment_status": "PENDING"
        },
        "error_report": {
            "available": bool(error_file),
            "file": error_file
        }
    }