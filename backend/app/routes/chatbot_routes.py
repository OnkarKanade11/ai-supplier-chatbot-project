from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database.connection import get_db
from ..services.chatbot_service import ChatbotService
from app.database.models import QueryRequest
  
 

router = APIRouter()
chatbot_service = ChatbotService()

@router.post("/query")
async def process_query(query: QueryRequest, db: Session = Depends(get_db)):
    # Access the query from the request body (query.query)
    response = chatbot_service.process_query(query.query, db)
    return {"message": response}
