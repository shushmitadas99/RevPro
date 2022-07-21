DROP TABLE IF EXISTS ers_reimbursements;
DROP TABLE IF EXISTS ers_users;

CREATE TABLE ers_users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(20) NOT NULL,
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
    reimb_author INTEGER NOT NULL,
    reimb_resolver INTEGER,
    reimbursement_amount NUMERIC NOT NULL,
    submitted TIMESTAMP,
    resolved TIMESTAMP,
    status VARCHAR(7) NOT NULL,
    description VARCHAR(100) NOT NULL,
      receipt BYTEA,
    CONSTRAINT fk_ers_users FOREIGN KEY (reimb_author) REFERENCES ers_users(user_id),
    CONSTRAINT fk_ers_users_reimb FOREIGN KEY (reimb_resolver) REFERENCES ers_users(user_id)
);

insert into ers_reimbursements (reimb_author, reimb_resolver, reimbursement_amount, status, description) values(3, 1, 1000, 'pending', 'lodging');
insert into ers_reimbursements (reimb_author, reimb_resolver, reimbursement_amount, status, description) values(3, 1, 2000, 'pending', 'travel');
insert into ers_reimbursements (reimb_author, reimb_resolver, reimbursement_amount, status, description) values(3, 1, 1000, 'pending', 'food');

SELECT * FROM ers_users;
SELECT * FROM ers_reimbursements;