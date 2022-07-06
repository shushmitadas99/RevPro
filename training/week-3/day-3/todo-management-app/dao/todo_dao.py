from dotenv import dotenv_values
from model.todo import Todo
import psycopg

config = dotenv_values(".env")  # is a dict

class TodoDao:

    def get_all_todos_by_user_id(self, user_id):
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
                cur.execute("SELECT * FROM todos WHERE user_id = %s", (user_id,))

                todo_list = []

                for row in cur:
                    todo_list.append(Todo(row[0], row[1], row[2], row[3]))

                return todo_list
