from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import chatbot_routes, product_routes
from app.database.connection import engine, Base
from app.config import Settings

# Create an instance of the Settings class
settings = Settings()

# Initialize FastAPI with the project title from Settings, using a default value if missing
app = FastAPI(title=settings.PROJECT_TITLE or "AI-Powered Chatbot")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for now, can be restricted for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create database tables
Base.metadata.create_all(bind=engine)

# Include routers for chatbot and product routes
app.include_router(chatbot_routes.router)
app.include_router(product_routes.router)

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
