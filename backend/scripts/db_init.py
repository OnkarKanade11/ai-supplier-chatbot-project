import sys
import os

# Add the project root directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sqlalchemy import create_engine
from app.database.connection import Base
from app.database.models import Supplier, Product
from app.config import settings

# Debugging: Print current configuration and paths
print(f"Current working directory: {os.getcwd()}")
print(f"Database URL: {settings.DATABASE_URL}")

def initialize_database():
    try:
        print("Initializing the database...")
        engine = create_engine(settings.DATABASE_URL)
        print("Database engine created successfully.")
        
        print("Creating tables...")
        Base.metadata.create_all(bind=engine)
        print("Database tables created successfully.")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    print("Starting database initialization script...")
    initialize_database()
