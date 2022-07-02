from flask import Flask
from controller.user_controller import uc  # controller(package).user_controller(file_name) import uc(var)

if __name__ == '__main__':  #__main__ => initial starting point of program execution
    app = Flask(__name__)  # The obj that gives you access to your web server

    # every endpoint we create needs to somehow map to the 'Flask' object
    app.register_blueprint(uc)  # Blueprint allows us register our endpoints with 'Flask' class object

    app.run(port=8080, debug=True)  # Starts up your web server
