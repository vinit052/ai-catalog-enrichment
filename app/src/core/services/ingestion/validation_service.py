from validators.product_import_validator import (
    ProductImportValidator,
    ValidationStatus,
)

class ValidationResult:
    def __init__(
        self,
        valid_records,
        invalid_records,
    ):
        self.valid_records = valid_records
        self.invalid_records = invalid_records

class ValidationService:
    def validate(self, records):
        result = (
            ProductImportValidator()
            .validate(
                None,
                records,
            )
        )

        valid = []
        invalid = []

        for row in result["rows"]:
            if row["status"] == ValidationStatus.VALID:
                valid.append(row["data"])
            else:
                invalid.append(row)

        return ValidationResult(
            valid,
            invalid,
        )