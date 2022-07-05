DROP TABLE IF EXISTS customers;

CREATE TABLE customers (
	id SERIAL PRIMARY KEY,
	first_name VARCHAR(30) UNIQUE NOT NULL,
	last_name VARCHAR(30) NOT NULL,
	mobile_phone VARCHAR(12) NOT NULL CHECK(mobile_phone SIMILAR TO '[0-9]{3}-[0-9]{3}-[0-9]{4}'),
	email VARCHAR(50) UNIQUE NOT NULL CHECK (email ~* '^[A-Za-z0-9._+%-]+@[A-Za-z0-9.-]+[.][A-Za-z]+$')
--	CONSTRAINT email CHECK (email ~* '^[A-Za-z0-9._+%-]+@[A-Za-z0-9.-]+[.][A-Za-z]+$')

);

INSERT INTO customers (first_name, last_name, mobile_phone, email)
VALUES 
('Shushmita', 'Das', '647-829-0001', 'shushmita99@github.com'),
('Bach', 'Tran', '512-826-0002', 'bachy21@revature.com'),
('Carol', 'Danvers', '437-876-0003', 'marvel@avengers.com');

SELECT * 
FROM customers