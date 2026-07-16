from enum import Enum


class ValidationStatus(str, Enum):
    VALID = "VALID"
    PARTIAL_VALID = "PARTIAL_VALID"
    INVALID = "INVALID"


class ProductImportValidator:

    REQUIRED_FIELDS = [
        "title",
        "description"
    ]

    def validate(self, import_id, records):

        results = []

        for index, record in enumerate(records):

            errors = []
            warnings = []

            # Required field validation
            for field in  self.REQUIRED_FIELDS:

                if not record.get(field):
                    errors.append(
                        {
                            "field": field,
                            "message": "Required field missing"
                        }
                    )


            # Future validations
            #
            # if not image:
            #     warnings.append({
            #        "field": "image",
            #        "message": "Image missing"
            #     })
            #
            # if sku invalid:
            #     errors.append(...)


            if errors:
                status = ValidationStatus.INVALID

            elif warnings:
                status = ValidationStatus.PARTIAL_VALID

            else:
                status = ValidationStatus.VALID

           
            results.append(
                {
                    "row": index + 1,
                    "status": status,
                    "errors": errors,
                    "warnings": warnings,
                    "data": record
                }
            )


        #return self._summary(results), results

        return {
             "rows": results,
            "summary": self._summary(results)
        }

    def _summary(self, results):

        summary = {
            "total": len(results),
            "valid": 0,
            "partial_valid": 0,
            "invalid": 0
        }

        for item in results:

            if item["status"] == ValidationStatus.VALID:
                summary["valid"] += 1

            elif item["status"] == ValidationStatus.PARTIAL_VALID:
                summary["partial_valid"] += 1

            else:
                summary["invalid"] += 1

        return summary