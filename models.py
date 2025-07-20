from pydantic import BaseModel, Field
from typing import List, Optional
from bson import ObjectId

class Product(BaseModel):
    name: str
    size: Optional[str] = Field(default=None)

class ProductInDB(Product):
    id: str

class Order(BaseModel):
    user_id: str
    product_ids: List[str]

class OrderInDB(Order):
    id: str
