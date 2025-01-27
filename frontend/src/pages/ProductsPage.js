import React, { useState, useEffect } from 'react';
import { productService } from '../services/api';  // Ensure productService is correctly imported
import ProductCard from '../components/ProductCard';

const ProductsPage = () => {
  const [products, setProducts] = useState([]);
  const [filters, setFilters] = useState({});

  useEffect(() => {
    const fetchProducts = async () => {
      try {
        const response = await productService.getProducts(filters);
        setProducts(response);  // Assuming the response is an array of products
      } catch (error) {
        console.error('Failed to fetch products:', error);
      }
    };

    fetchProducts();
  }, [filters]);  // Re-fetch when filters change

  return (
    <div className="products-page">
      <h1>Product Catalog</h1>
      <div className="filters">
        {/* Add filters UI here */}
        <button onClick={() => setFilters({ brand: 'Some Brand' })}>Filter by Brand</button>
      </div>
      <div className="product-list">
        {products.map((product) => (
          <ProductCard key={product.id} product={product} />
        ))}
      </div>
    </div>
  );
};

export default ProductsPage;
