-- my_p0_restful_api database queries

-- drop tables if already exists
DROP TABLE IF EXISTS accounts;
DROP TABLE IF EXISTS account_type;
DROP TABLE IF EXISTS customers;

-- Customers table
CREATE TABLE customers (
	id SERIAL PRIMARY KEY,
	first_name VARCHAR(30) UNIQUE NOT NULL,
	last_name VARCHAR(30) NOT NULL,
	mobile_phone VARCHAR(12) NOT NULL CHECK(mobile_phone SIMILAR TO '[0-9]{3}-[0-9]{3}-[0-9]{4}'),
	email VARCHAR(50) UNIQUE NOT NULL CHECK (email ~* '^[A-Za-z0-9._+%-]+@[A-Za-z0-9.-]+[.][A-Za-z]+$')
);

INSERT INTO customers (first_name, last_name, mobile_phone, email)
VALUES 
('Shushmita', 'Das', '647-829-0001', 'shushmita99@github.com'),
('Bach', 'Tran', '512-826-0002', 'bachy21@revature.com'),
('Carol', 'Danvers', '437-876-0003', 'marvel@avengers.com');

-- Account Type Table
CREATE TABLE account_type (
    id SERIAL PRIMARY KEY,
    type VARCHAR(20) NOT NULL
);

INSERT INTO account_type (type)
VALUES ('checking'),
('savings');

-- Accounts Table
CREATE TABLE accounts (
    id SERIAL PRIMARY KEY,  -- account_id
    balance INTEGER NOT NULL,
    customer_id INTEGER NOT NULL,
    account_type_id INTEGER NOT NULL,
    CONSTRAINT fk_customers FOREIGN KEY (customer_id) REFERENCES customers(id),
    CONSTRAINT fk_account_type FOREIGN KEY (account_type_id) REFERENCES account_type(id)
);

INSERT INTO accounts (balance, customer_id, account_type_id)
VALUES 
(1000, 1, 1),
(2000, 1, 2),
(125000, 2, 2);

-- SQL queries to display tables
SELECT * 
FROM customers

SELECT * 
FROM accounts

SELECT * 
FROM account_type

SELECT customers.id, customers.first_name, customers.last_name, accounts.balance, accounts.account_type_id
FROM customers
LEFT JOIN accounts ON customers.id = accounts.customer_id
ORDER BY customers.last_name;