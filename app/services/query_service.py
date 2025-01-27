from sqlalchemy.orm import Session
from ..database.models import Product, Supplier

def search_products(query: str, db: Session):
    print(f"Searching for products with query: {query}")
    return db.query(Product).filter(
        Product.name.ilike(f"%{query}%") | 
        Product.brand.ilike(f"%{query}%")
    ).all()
    
def search_suppliers(query: str, db: Session):
    print(f"Searching for suppliers with query: {query}")
    return db.query(Supplier).filter(
        Supplier.name.ilike(f"%{query}%") | 
        Supplier.product_categories.ilike(f"%{query}%")
    ).all()