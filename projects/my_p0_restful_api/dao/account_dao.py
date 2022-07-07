from dotenv import dotenv_values
from model.account import Account
import psycopg

config = dotenv_values(".env")  # is a dict


class AccountDao:

    def get_all_accounts_by_customer_id(self, customer_id):
        # Step 1: open a connection object
        with psycopg.connect(
                host=config['host'],
                port=config['port'],
                dbname=config['dbname'],
                user=config['user'],
                password=config['password']
        ) as conn:
            # Automatically close the cursor
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM accounts WHERE customer_id = %s", (customer_id,))

                account_list = []

                for row in cur:
                    account_list.append(Account(row[0], row[1], row[2], row[3]))

                return account_list

    def get_account_by_account_id(self, account_id):
        with psycopg.connect(
                host=config['host'],
                port=config['port'],
                dbname=config['dbname'],
                user=config['user'],
                password=config['password']
        ) as conn:
            # Automatically close the cursor
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM accounts WHERE id = %s", (account_id,))  # Tuple with one element

                account_row = cur.fetchone()  # return None if no record is found
                if not account_row:  # None is a falsy value, so not None is true
                    return None  # immediately return from this function and don't execute the rest of the code

                a_id = account_row[0]  # you don't want to replace the user_id in tuple above
                balance = account_row[1]
                customer_id = account_row[2]
                account_type_id = account_row[3]

                return Account(a_id, balance, customer_id, account_type_id)

    def get_customers_account_by_account_id(self, customer_id, account_id):
        with psycopg.connect(
                host=config['host'],
                port=config['port'],
                dbname=config['dbname'],
                user=config['user'],
                password=config['password']
        ) as conn:
            # Automatically close the cursor
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM accounts WHERE customer_id = %s AND id = %s", (customer_id, account_id,))  # Tuple with one element

                account_row = cur.fetchone()  # return None if no record is found
                if not account_row:  # None is a falsy value, so not None is true
                    return None  # immediately return from this function and don't execute the rest of the code

                a_id = account_row[0]  # you don't want to replace the user_id in tuple above
                balance = account_row[1]
                customer_id = account_row[2]
                account_type_id = account_row[3]

                return Account(a_id, balance, customer_id, account_type_id)
