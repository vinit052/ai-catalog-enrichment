from fastapi import APIRouter, UploadFile, File, HTTPException

from services.file_service import (
    validate_file,
    save_file,
)

router = APIRouter()

@router.post(
    "/upload",
    summary="Upload product file",
    description="""
Upload product catalog files.

Supported:
- CSV
- Excel
- Images
""",
)
async def upload_product_file(
    file: UploadFile = File(...)
):

    if not validate_file(file.filename):
        raise HTTPException(
            status_code=400,
            detail="Unsupported file type",
        )

    result = save_file(file)

    return {
        "message": "File uploaded successfully",
        "file": result,
    }