DROP TABLE IF EXISTS ers_reimbursements;
DROP TABLE IF EXISTS ers_users;

CREATE TABLE ers_users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(20) UNIQUE NOT NULL,
    password VARCHAR(60) NOT NULL,
    first_name VARCHAR(30) UNIQUE NOT NULL,
    last_name VARCHAR(30) NOT NULL,
    user_role VARCHAR(15) NOT NULL,
    email VARCHAR(50) UNIQUE NOT NULL CHECK (email ~* '^[A-Za-z0-9.+%-]+@[A-Za-z0-9.-]+[.][A-Za-z]+$'));

INSERT INTO ers_users (username, password, first_name, last_name, user_role, email)
VALUES 
('Shushmita97', crypt('ukygkgKYUGgugfog', gen_salt('bf')), 'Shushmita','Das', 'finance_manager', 'shushmita99@github.com'),
('Quinton98', crypt('bhgHGHJGghjkg', gen_salt('bf')), 'Quinton', 'Lott', 'finance_manager', 'quinton56@fibonacci.com'),
('Carol88', crypt('ggFJHVYYVYU', gen_salt('bf')), 'Carol', 'Danvers', 'employee', 'abc578f@randommail.com'),
('John', crypt('igukgUFYUKVyukguy', gen_salt('bf')), 'John', 'Danvers', 'employee', 'abcdefgh@revature.com');


--drop table if exists
CREATE TABLE ers_reimbursements (
    reimb_id SERIAL PRIMARY KEY,
    reimb_author VARCHAR(20) NOT NULL,
    reimb_resolver VARCHAR(20),
    reimbursement_amount NUMERIC NOT NULL,
    submitted TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    resolved TIMESTAMP,
    status VARCHAR(10) CHECK (status in ('pending', 'approved', 'denied')) DEFAULT 'pending',
    reimb_type VARCHAR(20) NOT NULL CHECK (reimb_type in ('Lodging','Travel', 'Food', 'Other')),
    description VARCHAR(100) NOT NULL,
    receipt BYTEA,
    CONSTRAINT fk_ers_users FOREIGN KEY (reimb_author) REFERENCES ers_users(username),
    CONSTRAINT fk_ers_users_reimb FOREIGN KEY (reimb_resolver) REFERENCES ers_users(username)
);

--status VARCHAR(15) CHECK (status in ('pending', 'approved', 'denied')) DEFAULT 'pending',
--reimb_type VARCHAR NOT NULL CHECK (reimb_type in ('Lodging','Travel', 'Food', 'Other')),

-- finance_manager => update reimbursement status 
--UPDATE reimbursements
--SET status = 'approved', resolved = CURRENT_TIMESTAMP
--WHERE reimb_id = 1;


insert into ers_reimbursements (reimb_author, reimbursement_amount, reimb_type, description) 
values('Shushmita97', 1678, 'Lodging', 'This is lodging');
insert into ers_reimbursements (reimb_author, reimbursement_amount, reimb_type, description) 
values('Carol88', 3444, 'Travel', 'This is travelling');
--insert into ers_reimbursements (reimb_author, reimb_resolver, reimbursement_amount, status, reimb_type, description) values(3, 1, 2000, 'pending', 'travel', 'This is travel');
--insert into ers_reimbursements (reimb_author, reimb_resolver, reimbursement_amount, status, reimb_type, description) values(3, 1, 1000, 'pending', 'food', 'This is food');
--insert into ers_reimbursements (reimb_author, reimbursement_amount, submitted, status, reimb_type, description)
--values(1, 1000, CURRENT_TIMESTAMP, 'pending', 'food', 'This is food expense');
--insert into ers_reimbursements (reimb_author, reimbursement_amount, submitted, status, reimb_type, description) "
--                    "values(1, 3000, CURRENT_TIMESTAMP, 'pending', 'travel', 'This is travel expense') WHERE ers_reimbursements.reimb_author == ers_users.username reimb_author IN (SELECT username FROM ers_users) RETURNING *);
                    
SELECT * FROM ers_users;
SELECT * FROM ers_reimbursements;

SELECT * FROM ers_reimbursements
WHERE reimb_author = 'Carol88';

SELECT * FROM ers_reimbursements WHERE reimb_author = 'Shushmita97' ORDER BY reimb_id ASC;

SELECT ers_users.username, ers_users.first_name, ers_users.last_name, ers_reimbursements.reimb_author, 
ers_reimbursements.reimb_resolver, ers_reimbursements.reimbursement_amount, ers_reimbursements.submitted, 
ers_reimbursements.resolved, ers_reimbursements.status, ers_reimbursements.reimb_type, 
ers_reimbursements.description, ers_reimbursements.receipt
FROM ers_users
LEFT JOIN ers_reimbursements ON ers_users.username = ers_reimbursements.reimb_author
GROUP BY ers_users.username
ORDER BY ers_reimbursements.reimb_id ASC;
