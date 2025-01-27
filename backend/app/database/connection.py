from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import settings  # Import the settings

# Database engine using the DATABASE_URL from settings
engine = create_engine(settings.DATABASE_URL)

# Base class for all models
Base = declarative_base()

# SessionLocal to interact with the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency to get the database session
def get_db():
    db = SessionLocal()  # Create a new session
    try:
        yield db  # Yield the session for use in the route
    finally:
        db.close()  # Close the session once done
