from core.infra.database.models.import_model import Import


def create_import_model(
    filename: str,
    total_records: int,
    valid_records: int,
    invalid_records: int,
) -> Import:

    return Import(
        filename=filename,
        total_records=total_records,
        valid_records=valid_records,
        invalid_records=invalid_records,
        status="PROCESSING",
    )