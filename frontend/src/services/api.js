import axios from 'axios';

const API_BASE_URL = process.env.REACT_APP_API_BASE_URL || 'http://localhost:8000';

const apiClient = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Chatbot service for sending queries
export const chatbotService = {
  sendQuery: async (query) => {
    const response = await apiClient.post('/query', { query }); // Send query as part of the body
    return response.data;
  },
};

// Product service for fetching products
export const productService = {
  getProducts: async (filters = {}) => {
    const response = await apiClient.get('/products', { params: filters });
    return response.data;
  },
};
