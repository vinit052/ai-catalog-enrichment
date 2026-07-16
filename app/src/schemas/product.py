from pydantic import BaseModel

class ProductSchema(BaseModel):

    title: str
    description: str
    image: str | None = None
    thumbnail: str | None = None