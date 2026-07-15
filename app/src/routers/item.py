from fastapi import APIRouter


router = APIRouter(
    prefix="/products",
    tags=["Products"]
)


@router.get("")
async def products():

    return {
        "message": "Product API"
    }