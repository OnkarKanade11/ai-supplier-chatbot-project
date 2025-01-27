from app.services.chatbot_service import ChatbotService
from app.database.connection import SessionLocal

def test_chatbot_query():
    db = SessionLocal()
    chatbot = ChatbotService()
    
    response = chatbot.process_query("laptops", db)
    assert response is not None
    db.close()