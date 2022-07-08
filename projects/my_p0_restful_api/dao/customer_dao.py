from dotenv import dotenv_values
from model.customer import Customer
import psycopg

config = dotenv_values(".env")  # is a dict


class CustomerDao:

    def create_customer(self, customer_object):  # user will represent a User object
        first_name_to_add = customer_object.first_name
        last_name_to_add = customer_object.last_name
        mobile_phone_to_add = customer_object.mobile_phone
        email_to_add = customer_object.email

        with psycopg.connect(
            host=config['host'],
            port=config['port'],
            dbname=config['dbname'],
            user=config['user'],
            password=config['password']
        ) as conn:
            # Automatically close the cursor
            with conn.cursor() as cur:
                cur.execute("INSERT INTO customers (first_name, last_name, mobile_phone, email) VALUES (%s, %s, %s, %s) RETURNING *",
                            (first_name_to_add, last_name_to_add, mobile_phone_to_add, email_to_add))  # Tuple

                inserted_customer_row = cur.fetchone()

                conn.commit()  # commit the transaction in any DML operation

                return Customer(inserted_customer_row[0], inserted_customer_row[1],
                            inserted_customer_row[2], inserted_customer_row[3], inserted_customer_row[4])

    def get_customers(self):
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
                cur.execute("SELECT * FROM customers ORDER BY customers.id ASC")

                my_list_of_user_objs = []
                # iterate over each row of the "users" table
                for customer in cur:
                    id = customer[0]
                    first_name = customer[1]
                    last_name = customer[2]
                    mobile_phone = customer[3]
                    email = customer[4]

                    my_user_obj = Customer(id, first_name, last_name, mobile_phone, email)
                    my_list_of_user_objs.append(my_user_obj)

                return my_list_of_user_objs

    def get_customer_by_id(self, customer_id):
        with psycopg.connect(
                host=config['host'],
                port=config['port'],
                dbname=config['dbname'],
                user=config['user'],
                password=config['password']
        ) as conn:
            # Automatically close the cursor
            with conn.cursor() as cur:

                cur.execute("SELECT * FROM customers WHERE id = %s", (customer_id,))  # Tuple with one element

                customer_row = cur.fetchone()  # return None if no record is found
                if not customer_row:  # None is a falsy value, so not None is true
                    return None  # immediately return from this function and don't execute the rest of the code

                c_id = customer_row[0]  # you don't want to replace the user_id in tuple above
                first_name = customer_row[1]
                last_name = customer_row[2]
                mobile_phone = customer_row[3]
                email = customer_row[4]

                return Customer(c_id, first_name, last_name, mobile_phone, email)

    # Pass the customer_object as argument for updating it using PUT method call
    def update_customer_by_id(self, customer_object):
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
                    "UPDATE customers SET first_name = %s, last_name = %s, mobile_phone = %s, email = %s WHERE id = %s RETURNING *",
                    (customer_object.first_name, customer_object.last_name, customer_object.mobile_phone,
                     customer_object.email, customer_object.id))

                conn.commit()

                updated_customer_row = cur.fetchone()

                if updated_customer_row is None:
                    return None

                return Customer(updated_customer_row[0], updated_customer_row[1], updated_customer_row[2],
                                updated_customer_row[3], updated_customer_row[4])

    # return True if a customer was deleted
    # return False if a customer was not deleted
    def delete_customer_by_id(self, customer_id):
        with psycopg.connect(
            host=config['host'],
            port=config['port'],
            dbname=config['dbname'],
            user=config['user'],
            password=config['password']
        ) as conn:
            # Automatically close the cursor
            with conn.cursor() as cur:
                cur.execute("DELETE FROM customers where id = %s", (customer_id,))  # Tuple with single value

                # Check number of rows that were deleted
                rows_deleted = cur.rowcount

                if rows_deleted != 1:
                    return False
                else:
                    conn.commit()  # commit the transaction
                    return True
