class ResponseBuilder:

    @staticmethod
    def success(
        import_id,
        filename,
        validation,
    ):
        return {
            "success": True,
            "data": {
                "import_id": import_id,
                "filename": filename,
                "summary": {
                    "total_records":(len(validation.valid_records)+len(validation.invalid_records)),
                    "valid_records":len(validation.valid_records),
                    "invalid_records":len(validation.invalid_records),
                },
                "processing": {
                    "storage": "COMPLETED",
                    "enrichment": "PENDING",
                }
            },
            "error": None
        }