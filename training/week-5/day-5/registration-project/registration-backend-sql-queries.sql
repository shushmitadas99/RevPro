DROP TABLE IF EXISTS users;

CREATE TABLE users (
	username VARCHAR(20) PRIMARY KEY,
	password VARCHAR(20) NOT NULL,
	first_name VARCHAR(100) NOT NULL,
	last_name VARCHAR(100) NOT NULL,
	gender VARCHAR(20) NOT NULL,
	phone_number VARCHAR(20) NOT NULL,
	email_address VARCHAR(200) NOT NULL UNIQUE
);

SELECT *
FROM users;