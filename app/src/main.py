from fastapi import FastAPI

from core.config import settings
from routers import health, upload


app = FastAPI(
    title="AI Catalog Enrichment API",
    description="""
API for AI-powered product catalog enrichment.

Supports:
- Product file upload
- CSV processing
- Excel processing
- Image processing
- Vector enrichment
""",
    version="1.0.0",
)


app.include_router(health.router)
app.include_router(upload.router)


@app.get("/", tags=["System"])
async def home():
    return {
        "name": settings.app.NAME,
        "status": "running",
        "environment": settings.app.ENV,
    }