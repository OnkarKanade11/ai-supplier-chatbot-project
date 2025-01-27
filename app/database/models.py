from sqlalchemy import Column, Integer, String, Float, Text, ForeignKey
from sqlalchemy.orm import relationship
from .connection import Base
from pydantic import BaseModel
from typing import List, Optional

class QueryRequest(BaseModel):
    query: str 
    
class Supplier(Base):
    __tablename__ = 'suppliers'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    contact_email = Column(String(255))
    phone_number = Column(String(20))
    product_categories = Column(Text)
    
    products = relationship("Product", back_populates="supplier")

class Product(Base):
    __tablename__ = 'products'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    brand = Column(String(100))
    price = Column(Float)
    category = Column(String(100))
    description = Column(Text)
    supplier_id = Column(Integer, ForeignKey('suppliers.id'))
    
    supplier = relationship("Supplier", back_populates="products")