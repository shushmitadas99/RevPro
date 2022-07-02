from dotenv import dotenv_values
from model.user import User
import psycopg

config = dotenv_values(".env") # is a dict


# structure the above dict in OOP way using class
class UserDao:
    # CRUD operations
    # Create - Insert a new user into our "database"
    # Read   - Retrieve a user or users from our "database"
    # Update - Update a user in our "database"
    # Delete - Delete a user in our "database"

    # The "with" keyword will allow us to automatically close the connection object whenever we are done executing
    # the block of code established using the "with" keyword
    def get_all_users(self):
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
                cur.execute("SELECT * FROM users")

                my_list_of_user_objs = []
                # iterate over each row of the "users" table
                for user in cur:
                    id = user[0]
                    username = user[1]
                    mobile_phone = user[2]
                    active = user[3]

                    my_user_obj = User(id, username, mobile_phone, active)
                    my_list_of_user_objs.append(my_user_obj)

                return my_list_of_user_objs

    def add_user(self, user_object):  # user will represent a User object
        username_to_add = user_object.username
        mobile_phone_to_add = user_object.mobile_phone

        with psycopg.connect(
            host=config['host'],
            port=config['port'],
            dbname=config['dbname'],
            user=config['user'],
            password=config['password']
        ) as conn:
            # Automatically close the cursor
            with conn.cursor() as cur:
                cur.execute("INSERT INTO users (username, mobile_phone) VALUES (%s, %s) RETURNING *",
                            (username_to_add, mobile_phone_to_add))  # Tuple
                user_row_that_was_just_inserted = cur.fetchone()

                return User(user_row_that_was_just_inserted[0], user_row_that_was_just_inserted[1],
                            user_row_that_was_just_inserted[2], user_row_that_was_just_inserted[3])

    def get_user_by_id(self, user_id):
        with psycopg.connect(
                host=config['host'],
                port=config['port'],
                dbname=config['dbname'],
                user=config['user'],
                password=config['password']
        ) as conn:
            # Automatically close the cursor
            with conn.cursor() as cur:

                cur.execute("SELECT * FROM users WHERE id = %s", (user_id,))  # Tuple with one element

                user_row = cur.fetchone()  # return None if no record is found
                if not user_row:  # None is a falsy value, so not None is true
                    return None  # immediately return from this function and don't execute the rest of the code

                u_id = user_row[0]  # you don't want to replace the user_id in tuple above
                username = user_row[1]
                mobile_phone = user_row[2]
                active = user_row[3]

                return User(u_id, username, mobile_phone, active)

