import React, { useState } from 'react';
import { chatbotService } from '../services/api';  // Correct import

const ChatbotPage = () => {
  const [query, setQuery] = useState('');
  const [response, setResponse] = useState('');
  const [loading, setLoading] = useState(false);

  const handleQueryChange = (e) => {
    setQuery(e.target.value);
  };

  const handleSendQuery = async () => {
    if (!query) return;

    setLoading(true);
    try {
      // Send query to backend using chatbotService
      const result = await chatbotService.sendQuery({ query: query });
      setResponse(result.message);  // Assuming the backend returns a message key in the response
    } catch (error) {
      setResponse('Error: Unable to process the query.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="chatbot-container">
      <div className="chatbox">
        <div className="query">
          <input
            type="text"
            value={query}
            onChange={handleQueryChange}
            placeholder="Ask about products or suppliers"
          />
          <button onClick={handleSendQuery}>Send</button>
        </div>
        {loading ? <p>Loading...</p> : <p>{response}</p>}
      </div>
    </div>
  );
};

export default ChatbotPage;
