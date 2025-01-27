from pydantic import BaseModel
from typing import Optional, List

# Base schemas for Supplier and Product data
class SupplierBase(BaseModel):
    name: str
    contact_email: Optional[str] = None
    phone_number: Optional[str] = None
    product_categories: Optional[str] = None

class ProductBase(BaseModel):
    name: str
    brand: Optional[str] = None
    price: float
    category: Optional[str] = None
    description: Optional[str] = None
    supplier_id: Optional[int] = None

# Response schemas (include 'id' and ORM configuration for converting SQLAlchemy models)
class ProductResponse(ProductBase):
    id: int

    class Config:
        orm_mode = True  # Tells Pydantic to treat this as an ORM model

class SupplierResponse(SupplierBase):
    id: int
    products: List[ProductResponse] = []  # Including related products as a list of ProductResponse

    class Config:
        orm_mode = True  # Tells Pydantic to treat this as an ORM model

# Request schema for query input
class QueryRequest(BaseModel):
    query: str

    class Config:
        orm_mode = True
