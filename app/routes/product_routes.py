from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database.connection import get_db
from ..database.models import Product, Supplier
from ..database.schemas import ProductResponse

router = APIRouter()

@router.get("/products")
async def get_products(
    brand: str = None, 
    category: str = None, 
    db: Session = Depends(get_db)
):
    query = db.query(Product)  # Query for all products
    
    if brand:
        query = query.filter(Product.brand == brand)  # Filter by brand if provided
    if category:
        query = query.filter(Product.category == category)  # Filter by category if provided
    
    products = query.all()  # Get the products from the database
    return [ProductResponse.from_orm(product) for product in products]  # Convert to ProductResponse
