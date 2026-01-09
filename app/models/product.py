from pydantic import BaseModel, Field
from typing import Optional

class Product(BaseModel):
    id: Optional[int] = None
    name: str = Field(..., min_length=1, max_length=200)
    price: float = Field(..., gt=0)
    stock: int = Field(..., ge=0)
    category: Optional[str] = None
    description: Optional[str] = None

    class Config:
        json_schema_extra = {
            "example": {
                "name": "Leche Entera 1L",
                "price": 1.20,
                "stock": 100,
                "category": "Lácteos",
                "description": "Leche entera fresca"
            }
        }
