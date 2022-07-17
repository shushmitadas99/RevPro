DROP TABLE if EXISTS employees;

CREATE TABLE employees (
	id SERIAL PRIMARY KEY,
	salary INTEGER NOT NULL CHECK(salary > 0),
	first_name VARCHAR(100) NOT NULL,
	last_name VARCHAR(100) NOT NULL,
	department VARCHAR(50) NOT NULL
);

INSERT INTO employees (salary, first_name, last_name, department)
VALUES
(50000, 'Connie', 'Elliott', 'HR'),
(70000, 'John', 'Doe', 'HR'),
(75000, 'Jane', 'Doe', 'HR'),
(200000, 'Bob', 'Smith', 'C-Suite'),
(300000, 'Ashwin', 'Bharath', 'C-Suite'),
(120000, 'Michael', 'Minton', 'IT'),
(140000, 'Bach', 'Tran', 'IT'),
(110000, 'Sally', 'Kyle', 'IT');

SELECT *
FROM employees;

-- Aggregate Function Examples: MIN, MAX, AVG, SUM, COUNT
-- Aggregate functions take a bunch of values in different rows and reduces to a SINGLE VALUE
-- Many inputs | one output
SELECT MIN(salary)
FROM employees;

SELECT MAX(salary)
FROM employees;

SELECT AVG(salary)
FROM employees;

SELECT SUM(salary)
FROM employees;

SELECT COUNT(*)
FROM employees;

-- Get the average salary of each department
SELECT AVG(salary)
FROM employees
WHERE department = 'IT';

SELECT department, AVG(salary)
FROM employees
GROUP BY department;

-- Using ORDER BY to order results in ascending/descending order
SELECT department, AVG(salary)
FROM employees
GROUP BY department
ORDER BY AVG(salary) ASC;  -- Also the default

-- Get the minimum salary of each department
SELECT department, MIN(salary)
FROM employees
GROUP BY department;

-- Get the maximum salary of each department
SELECT department, MAX(salary)
FROM employees
GROUP BY department;

-- Scalar Functions Examples: LENGTH, CONCAT, ABS
-- Scalar functions act INDEPENDENTLY on each row 
-- One input | one output
SELECT LENGTH(first_name) as first_name_length  -- add alias first_name_length
FROM employees;

SELECT first_name, LENGTH(first_name) as first_name_length, salary, department, last_name  -- add alias first_name_length
FROM employees;

SELECT CONCAT(first_name, ' ', last_name) as full_name, salary, department
FROM employees;

SELECT ABS(salary)
FROM employees;

--ORDER BY length of full name
SELECT * 
FROM employees 
ORDER BY LENGTH(CONCAT(first_name, ' ', last_name));  -- Doesn't actually print the full name
