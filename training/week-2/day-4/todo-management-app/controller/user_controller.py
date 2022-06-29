from flask import Blueprint, request
from model.user import User
from service.user_service import UserService
from exception.invalid_parameter import InvalidParameterError

uc = Blueprint('user_controller', __name__)  # variable
# user_dao = UserDao() # object => not required anymore as we import from user_service now
user_service = UserService()

# Note: We have to utilize the user_service.py methods from user_controller.py
# Always test if your endpoint is working on Postman before implementing them further


@uc.route('/users')
def get_all_users():
    return {
        "users": user_service.get_all_users()  # already a list of dictionaries
    }
    # not required as we import from user_service now
    # return {
    #     "users": list(map(lambda e: e.to_dict(), user_dao.get_all_users()))  # returns a list of User objects
    # }  # we cannot just return a list for JSON, so we have to tag "users" as key for the whole list
    # to make it a dict
    # the map function will iterate through our list of User onjects and individually transform each element
    # in this case, we are transforming each element into a dict using our custom to_dict() method inside User class
    # convert map object to a list to make it serializable


@uc.route('/users/<username>')
def get_user_by_username(username):
    try:
        return user_service.get_user_by_username(username)  # dictionary
    except KeyError as e:
        return{
            "message": f"User with username {username} was  not found!"
        }, 404
    # not required as we import from user_service now
    # return user_dao.get_user_by_username(username).to_dict()  # this method would work because it returns a dict
    # containing a single user's info unlike the previous endpoint method returning a list of users


@uc.route('/users', methods=['POST'])
def add_user():
    user_json_dictionary = request.get_json()  # need to import request from Flask
    user_object = User(user_json_dictionary['username'], user_json_dictionary['mobile_phone'])  # constructor
    try:
        return user_service.add_user(user_object), 201  # Dictionary representation of the newly added user
    except InvalidParameterError as e:
        return {
            "message": str(e)
        }, 400

    # 201 created

@uc.route('/users/<username>', methods=['PUT'])
def edit_user_by_username(username):
    user_json_dictionary = request.get_json()
    user_object = User(user_json_dictionary['username'], user_json_dictionary['mobile_phone'])  # constructor
    return user_service.edit_user_by_username(username, user_object)