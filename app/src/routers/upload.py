from fastapi import (
    APIRouter,
    File,
    HTTPException,
    UploadFile,
)

router = APIRouter(
    prefix="/upload",
    tags=["Upload"],
)

@router.post("/")
async def upload_product_file(
    file: UploadFile = File(...),
):
    try:
        # result = await process_file(
        #     file,
        #     import_service,
        # )
        return {
            "message": "File uploaded successfully",
            "filename": file.filename,
        }

    except ValueError as exc:
        raise HTTPException(
            status_code=400,
            detail=str(exc),
        )