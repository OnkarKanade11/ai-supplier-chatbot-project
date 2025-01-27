import React, { useContext } from 'react';
import { ChatContext } from '../context/ChatContext';

function QueryHistory() {
  const { messages } = useContext(ChatContext);

  return (
    <div className="p-4">
      <h2 className="text-xl font-bold mb-4">Query History</h2>
      {messages.slice(-10).map((msg, index) => (
        <div 
          key={index} 
          className={`mb-2 p-2 rounded ${
            msg.sender === 'user' ? 'bg-blue-100' : 'bg-gray-100'
          }`}
        >
          {msg.text}
        </div>
      ))}
    </div>
  );
}

export default QueryHistory;