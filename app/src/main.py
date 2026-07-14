from fastapi import FastAPI

from config import settings
from routers import health, products


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


app.include_router(
    health.router,
    prefix="/health",
    tags=["Health"],
)


app.include_router(
    products.router,
    prefix="/products",
    tags=["Products"],
)


@app.get(
    "/",
    tags=["System"],
)
def home():
    return {
        "name": "AI Catalog Enrichment API",
        "status": "running",
        "environment": settings.APP_ENV,
    }