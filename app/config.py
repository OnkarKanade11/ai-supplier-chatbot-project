from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_TITLE: str = "AI Supplier Chatbot"
    DATABASE_URL: str = "mysql+pymysql://root:root@localhost:3306/supplier_chatbot"
    SECRET_KEY: str = "abc123!@#DEF456$%^GHI789&*()JKL012<>?mno"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        env_file = ".env"

settings = Settings()