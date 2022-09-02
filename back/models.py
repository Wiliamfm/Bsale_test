from pydantic import BaseModel
from decimal import Decimal

class Category(BaseModel):
    id: int
    name: str

class Product(BaseModel):
    id: int
    name: str
    url_image: str | None
    price: Decimal
    discount: int
    category: Category