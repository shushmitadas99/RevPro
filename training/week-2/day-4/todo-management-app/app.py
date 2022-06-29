from flask import Flask
from controller.user_controller import uc  # controller(package).user_controller(file_name) import uc(var)

# __name__ is a special variable that contains a string representing a python file
# is being executed
# __name__ is just the name of the file itself

# The purpose of this if statement is so that if another file imports this file, then
# the code inside this if block will not run, since __name__ would not be __main__ in
# that situation
if __name__ == '__main__':  #__main__ => initla starting point of program execution
    app = Flask(__name__)  # The obj that gives you access to your web server

    # every endpoint we create needs to somehow map to the 'Flask' object
    app.register_blueprint(uc)  # Blueprint allows us register our endpoints with 'Flask' class object

    app.run(port=8080, debug=True)  # Starts up your web server
