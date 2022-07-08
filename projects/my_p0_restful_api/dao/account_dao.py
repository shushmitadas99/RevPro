from dotenv import dotenv_values
from model.account import Account
import psycopg

config = dotenv_values(".env")  # is a dict


class AccountDao:

    def create_account(self, account_object):  # user will represent a User object
        balance_to_add = account_object.balance
        customer_id_to_add = account_object.customer_id
        account_type_id_to_add = account_object.account_type_id

        # if customer_id == customer_id_to_add:

        with psycopg.connect(
            host=config['host'],
            port=config['port'],
            dbname=config['dbname'],
            user=config['user'],
            password=config['password']
        ) as conn:
            # Automatically close the cursor
            with conn.cursor() as cur:
                cur.execute("INSERT INTO accounts (balance, customer_id, account_type_id) VALUES (%s, %s, %s) RETURNING *",
                            (balance_to_add, customer_id_to_add, account_type_id_to_add))  # Tuple

                inserted_account_row = cur.fetchone()

                conn.commit()  # commit the transaction in any DML operation

                return Account(inserted_account_row[0], inserted_account_row[1],
                            inserted_account_row[2], inserted_account_row[3])


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
                cur.execute("SELECT * FROM accounts WHERE customer_id = %s ORDER BY accounts.id ASC", (customer_id,))

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

    def update_customer_account_by_account_id(self, account_object):
        with psycopg.connect(
                host=config['host'],
                port=config['port'],
                dbname=config['dbname'],
                user=config['user'],
                password=config['password']
        ) as conn:
            # Automatically close the cursor
            with conn.cursor() as cur:
                cur.execute(
                    "UPDATE accounts SET balance = %s WHERE customer_id = %s AND account_type_id = %s RETURNING *",
                    (account_object.balance, account_object.customer_id, account_object.account_type_id))

                conn.commit()

                updated_account_row = cur.fetchone()

                if updated_account_row is None:
                    return None

                return Account(updated_account_row[0], updated_account_row[1], updated_account_row[2],
                                updated_account_row[3])

    def delete_customer_account_by_account_id(self, customer_id, account_id):
        with psycopg.connect(
                host=config['host'],
                port=config['port'],
                dbname=config['dbname'],
                user=config['user'],
                password=config['password']
        ) as conn:
            # Automatically close the cursor
            with conn.cursor() as cur:
                cur.execute(
                    "DELETE FROM accounts where customer_id = %s AND id = %s", (customer_id, account_id))

                # Check number of rows that were deleted
                rows_deleted = cur.rowcount

                if rows_deleted != 1:
                    return False
                else:
                    conn.commit()  # commit the transaction
                    return True