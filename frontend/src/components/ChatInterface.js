import React, { useState, useContext } from 'react';
import { ChatContext } from '../context/ChatContext';
import { chatbotService } from '../services/api';

function ChatInterface() {
  const [query, setQuery] = useState('');
  const { messages, addMessage } = useContext(ChatContext);

  const handleSendQuery = async () => {
    if (!query.trim()) return;

    addMessage({ text: query, sender: 'user' });
    console.log("Sending query:", query);
    try {
      const response = await chatbotService.sendQuery(query);
      console.log(response);
      addMessage({ text: response.message, sender: 'bot' });
    } catch (error) {
      addMessage({ text: 'Error processing query', sender: 'bot' });
    }

    setQuery('');
  };

  return (
    <div className="flex flex-col h-full">
      <div className="flex-grow overflow-y-auto p-4">
        {messages.map((msg, index) => (
          <div 
            key={index} 
            className={`mb-2 p-2 rounded ${
              msg.sender === 'user' ? 'bg-blue-100 text-right' : 'bg-gray-100'
            }`}
          >
            {msg.text}
          </div>
        ))}
      </div>
      <div className="p-4 border-t">
        <input
          type="text"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          className="w-full p-2 border rounded"
          placeholder="Ask about products or suppliers"
        />
        <button 
          onClick={handleSendQuery}
          className="mt-2 w-full bg-blue-500 text-white p-2 rounded"
        >
          Send
        </button>
      </div>
    </div>
  );
}

export default ChatInterface;