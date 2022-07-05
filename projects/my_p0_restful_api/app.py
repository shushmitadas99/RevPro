from flask import Flask
from controller.customer_controller import cc

if __name__ == '__main__':
    app = Flask(__name__)

    app.register_blueprint(cc)  # Blueprint allows us register our endpoints with 'Flask' class object


    # Task 1 -  Create a simple flask app and run it
    # Task 2 - connect your flask app to your postgresql database
    # Task 3 - Create customers, accounts, transaction table using flask - models

app.run(port=8080, debug=True)  # Starts up your web server
