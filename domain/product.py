from pydantic import BaseModel
from typing import Optional

class Product(BaseModel):
    id: Optional[str]
    name: str
    description: str
    price: float
    photo_url: str
    deleted_at: Optional[float]