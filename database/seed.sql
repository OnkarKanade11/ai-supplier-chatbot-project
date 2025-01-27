-- Insert sample suppliers
INSERT INTO suppliers (name, contact_email, phone_number, product_categories) VALUES
('TechGiant Electronics', 'sales@techgiant.com', '1-800-TECH', 'Laptops, Smartphones'),
('GlobalWare Solutions', 'info@globalware.com', '1-888-GLOBAL', 'Enterprise Software');

-- Insert sample products
INSERT INTO products (name, brand, price, category, description, supplier_id) VALUES
('SuperBook Pro', 'TechGiant', 1299.99, 'Laptops', 'High-performance laptop', 1),
('GlobalCloud Enterprise', 'GlobalWare', 599.99, 'Software', 'Cloud management platform', 2);

-- Insert sample users (use password hashing in actual implementation)
INSERT INTO users (email, password) VALUES
('admin@example.com', 'hashed_password_here');