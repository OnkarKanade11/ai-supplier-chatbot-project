import sys
import os

# Add the project root directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sqlalchemy.orm import Session
from app.database.connection import SessionLocal
from app.database.models import Supplier, Product

def seed_database():
    db = SessionLocal()

    try:
        # Create Suppliers
        suppliers = [
            Supplier(
                name="TechGiant Electronics", 
                contact_email="info@techgiant.com", 
                phone_number="1-800-TECH", 
                product_categories="Laptops, Smartphones, Tablets"
            ),
            Supplier(
                name="GlobalWare Solutions", 
                contact_email="sales@globalware.com", 
                phone_number="1-888-GLOBAL", 
                product_categories="Enterprise Software, Cloud Services"
            )
        ]
        db.add_all(suppliers)
        db.commit()

        # Create Products
        products = [
            Product(
                name="SuperBook Pro", 
                brand="TechGiant", 
                price=1299.99, 
                category="Laptops", 
                description="High-performance laptop with latest processor",
                supplier_id=1  # This refers to the first supplier (TechGiant Electronics)
            ),
            Product(
                name="GlobalCloud Enterprise", 
                brand="GlobalWare", 
                price=599.99, 
                category="Cloud Services", 
                description="Comprehensive cloud management platform",
                supplier_id=2  # This refers to the second supplier (GlobalWare Solutions)
            )
        ]
        db.add_all(products)
        db.commit()

        print("Sample data seeded successfully.")
    
    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        db.close()

if __name__ == "__main__":
    seed_database()
