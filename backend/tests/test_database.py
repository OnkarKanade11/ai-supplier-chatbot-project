from app.database.models import Supplier, Product
from app.database.connection import SessionLocal

def test_create_supplier():
    db = SessionLocal()
    supplier = Supplier(name="Test Supplier", contact_email="test@example.com")
    db.add(supplier)
    db.commit()
    
    assert supplier.id is not None
    db.close()