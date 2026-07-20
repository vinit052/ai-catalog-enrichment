from fastapi import (
    APIRouter,
    File,
    HTTPException,
    UploadFile,
    Depends,
)

from core.services.ingestion.ingestion_service import IngestionService
from dependencies import get_ingestion_service

router = APIRouter(
    prefix="/imports",
    tags=["Imports"],
)

@router.post("/")
async def create_import(
    file: UploadFile = File(...),
    ingestion_service: IngestionService = Depends(
        get_ingestion_service
    ),
):

    return await ingestion_service.ingest(file)