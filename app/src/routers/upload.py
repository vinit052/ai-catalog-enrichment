from fastapi import (
    APIRouter,
    File,
    HTTPException,
    UploadFile,
    Depends,
)

from services.file_service import process_file

from core.services.import_service import ImportService
from dependencies import get_import_service


router = APIRouter(
    prefix="/upload",
    tags=["Upload"],
)


@router.post("/")
async def upload_product_file(
    file: UploadFile = File(...),
    import_service: ImportService = Depends(
        get_import_service
    ),
):

    try:

        result = await process_file(
            file,
            import_service,
        )

        return {
            "message": "File processed successfully",
            "data": result,
        }


    except ValueError as exc:

        raise HTTPException(
            status_code=400,
            detail=str(exc),
        )