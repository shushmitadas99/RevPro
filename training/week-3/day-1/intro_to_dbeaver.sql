-- Sublanguages of SQL
-- DCL
-- TCL
-- DQL
-- DML
-- DDL (Data Definition Language)

-- DDL is responsible for the creation, alteration, deletion of tables (and technically other database objects as well)
-- CREATE
-- ALTER
-- DROP 
-- TRUNCATE

-- Naming convention for table name:
-- 1. All lowercase
-- 2. No spwcial symbols
-- 3: Plural
-- 4. Use _ to seperate words

DROP TABLE IF EXISTS users;

CREATE TABLE users (
	id SERIAL PRIMARY KEY, -- col_name data_type constraints
	username VARCHAR(50) UNIQUE NOT NULL, 
	mobile_phone VARCHAR(12) NOT NULL CHECK(mobile_phone SIMILAR TO '[0-9]{3}-[0-9]{3}-[0-9]{4}'),
	active_user BOOLEAN DEFAULT true
);

-- DML is used to create, read, update, and delete rows inside of a table
-- INSERT 
-- SELECT 
-- UPDATE 
-- DELETE 

INSERT INTO users(username, mobile_phone)
VALUES 
('bachy21', '512-826-0001'),
('jane_doe', '512-826-0002');

INSERT INTO users(username, mobile_phone, active_user)
VALUES 
('bob123', '512-826-0001', false);

-- SELECT 
SELECT *
FROM users;

-- UPDATE
UPDATE users 
SET 
username = 'bachy111',
mobile_phone = '512-826-1111'
WHERE id = 1;

-- DELETE 
DELETE FROM users
WHERE id = 1;

TRUNCATE users;

-- Relationships

DROP TABLE IF EXISTS todos;

CREATE TABLE todos (
	id SERIAL PRIMARY KEY,
	description VARCHAR(200) NOT NULL,
	completed BOOLEAN NOT NULL DEFAULT false,
	user_id INTEGER NOT NULL,
	CONSTRAINT fk_users FOREIGN KEY (user_id) REFERENCES users(id)
);

SELECT *
FROM todos;

INSERT INTO todos(description, user_id)
VALUES
('Do laundry', 1),
('Create copy of house key', 1),
('Cook lunch', 2),
('Send email to Fred', 2),
('Pick up package', 2);

-- JOINS
-- INNER
-- FULL/OUTER
-- LEFT/RIGHT

SELECT *
FROM users
INNER JOIN todos
ON users.id = todos.user_id

SELECT *
FROM users
FULL OUTER JOIN todos
ON users.id = todos.user_id

SELECT users.username, todos.description
FROM users
INNER JOIN todos
ON users.id = todos.user_id

SELECT users.username, todos.description
FROM users
LEFT JOIN todos
ON users.id = todos.user_id

SELECT users.id as u_id, users.username, todos.description, todos.user_id
FROM users
LEFT JOIN todos
ON users.id = todos.user_id


SELECT users.id as u_id, users.username, todos.description, todos.user_id
FROM users
RIGHT JOIN todos
ON users.id = todos.user_id
