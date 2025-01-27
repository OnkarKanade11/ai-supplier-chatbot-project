from langchain.chat_models import ChatOpenAI
from ..config import settings

class LLMService:
    def __init__(self):
        self.llm = ChatOpenAI(
            api_key=settings.LLM_API_KEY, 
            model_name="gpt-3.5-turbo"
        )

    def generate_summary(self, text):
        prompt = f"Summarize the following text concisely: {text}"
        return self.llm.predict(prompt)