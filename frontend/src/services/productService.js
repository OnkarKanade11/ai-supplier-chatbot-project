import axios from 'axios';

const API_BASE_URL = process.env.REACT_APP_API_BASE_URL || 'http://localhost:8000';

const apiClient = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export const productService = {
  getProducts: async (filters) => {
    try {
      const response = await apiClient.get('/products', { params: filters });
      return response.data; // assuming the response contains the products array
    } catch (error) {
      console.error('Failed to fetch products:', error);
      throw error; // Ensure error handling
    }
  },
};
