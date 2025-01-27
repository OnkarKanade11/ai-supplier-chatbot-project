from langchain.chat_models import ChatOpenAI
from .query_service import search_products, search_suppliers

class ChatbotService:
    def __init__(self):
        self.llm = ChatOpenAI(
            model_name="gpt-3.5-turbo",
            openai_api_key="your_openai_api_key"
        )

    def process_query(self, query, db):
        # Print received query
        print(f"Received query: {query}")

        if "product" in query.lower():
            results = search_products(query, db)
        elif "supplier" in query.lower():
            results = search_suppliers(query, db)
        else:
            results = []

        # Print query results
        print(f"Query Results: {results}")
        
        response = self._generate_response(query, results)
        return response

    def _generate_response(self, query, results):
        if not results:
            return "Sorry, I couldn't find any matching information."
        formatted_results = "\n".join([str(item) for item in results])
        return formatted_results
