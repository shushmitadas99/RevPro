-- my_p1_ers_system database queries

-- CREATE EXTENSION pgcrypto; -- Extension for password encryption

-- drop tables if already exists
DROP TABLE IF EXISTS ers_reimbursements;
DROP TABLE IF EXISTS ers_users;

-- Users Table
CREATE TABLE ers_users (
	user_id SERIAL PRIMARY KEY,
	username VARCHAR(20) NOT NULL,
	password VARCHAR(60) NOT NULL,
	first_name VARCHAR(30) UNIQUE NOT NULL,
	last_name VARCHAR(30) NOT NULL,
	user_role VARCHAR(15) NOT NULL,
	email VARCHAR(50) UNIQUE NOT NULL CHECK (email ~* '^[A-Za-z0-9._+%-]+@[A-Za-z0-9.-]+[.][A-Za-z]+$')
);

INSERT INTO ers_users (username, password, first_name, last_name, user_role, email)
VALUES 
('Shushmita97', 'passWRD234', 'Shushmita','Das', 'finance_manager', 'shushmita99@github.com'),
('Quinton98', crypt('bhgHGHJGghjkg', gen_salt('bf')), 'Quinton', 'Lott', 'finance_manager', 'quinton56@fibonacci.com'),
('Carol88', crypt('ggFJHVYYVYU', gen_salt('bf')), 'Carol', 'Danvers', 'employee', 'abc578f@randommail.com'),
('John', crypt('igukgUFYUKVyukguy', gen_salt('bf')), 'John', 'Danvers', 'employee', 'abcdefgh@revature.com');

-- User Role Table
--CREATE TABLE user_role (
--    id SERIAL PRIMARY KEY,
--    type VARCHAR(20) NOT NULL
--);
--
--INSERT INTO user_role (type)
--VALUES ('Finance manager'),
--('Employee');

-- Reimbursements Table
CREATE TABLE ers_reimbursements (
    reimb_id SERIAL PRIMARY KEY,
    reimb_author INTEGER NOT NULL,
    reimb_resolver INTEGER,
    reimbursement_amount NUMERIC NOT NULL,
    submitted TIMESTAMP NOT NULL,
    resolved TIMESTAMP,
    status VARCHAR(7) NOT NULL,
    description VARCHAR(100) NOT NULL,
--    receipt BYTEA,
    CONSTRAINT fk_ers_users FOREIGN KEY (reimb_author) REFERENCES ers_users(user_id),
    CONSTRAINT fk_ers_users_reimb FOREIGN KEY (reimb_resolver) REFERENCES ers_users(user_id)
);

-- SQL queries to display tables -> Execute each separately
SELECT * 
FROM ers_users
ORDER BY user_id ASC;

SELECT * 
FROM ers_reimbursements
ORDER BY reimb_id ASC;
