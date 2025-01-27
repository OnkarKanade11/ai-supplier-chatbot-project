import React from 'react';
import { Link } from 'react-router-dom';

const Navbar = () => {
  return (
    <nav className="bg-gray-800 p-4">
      <ul className="flex space-x-4">
        <li>
          <Link to="/" className="text-white">Chatbot</Link>
        </li>
        <li>
          <Link to="/products" className="text-white">Products</Link>
        </li>
      </ul>
    </nav>
  );
};

export default Navbar;
