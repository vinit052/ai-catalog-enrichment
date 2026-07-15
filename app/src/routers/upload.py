import uuid
from fastapi import APIRouter, File, HTTPException, UploadFile
from services.file_service import process_file


router = APIRouter(
    prefix="/upload",
    tags=["Upload"],
)

def generate_import_id():
    return f"IMP-{uuid.uuid4().hex[:8].upper()}"

@router.post("/")
async def upload_product_file(
    file: UploadFile = File(...)
):
    import_id = generate_import_id()
    try:
        result = await process_file(file, import_id)

        return {
            "message": "File processed successfully",
            "data": result,
        }

    except ValueError as exc:
        raise HTTPException(
            status_code=400,
            detail=str(exc),
        )