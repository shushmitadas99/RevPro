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
