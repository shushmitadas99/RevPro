from flask import Blueprint, request
from model.user import User
from service.user_service import UserService
from exception.invalid_parameter import InvalidParameterError
from exception.user_not_found import UserNotFoundError

uc = Blueprint('user_controller', __name__)  # variable

# Instantiate a UserService object
user_service = UserService()

# Get all users (READ)
# Get user by id (READ)
# Add users (CREATE)
# Delete user by id (DELETE)
# Update user by id (UPDATE)


# Note: We have to utilize the user_service.py methods from user_controller.py
# Always test if your endpoint is working on Postman before implementing them further
@uc.route('/users')  # GET /users
def get_all_users():
    return {
        "users": user_service.get_all_users()  # already a list of dictionaries
    }


@uc.route('/users/<user_id>')  # GET /users/<user_id>
def get_user_by_id(user_id):
    try:
        return user_service.get_user_by_id(user_id)  # dictionary
    except UserNotFoundError as e:
        return {
                   "message": str(e)
               }, 404


@uc.route('/users/<user_id>', methods=['DELETE'])
def delete_user_by_id(user_id):
    try:
        user_service.delete_user_by_id(user_id)  # not a return value since we are not returning anything

        return {
            "message": f"User with id {user_id} deleted successfully"
        }
    except UserNotFoundError as e:  # Handles the exception that was raised in user_service layer
        return {
            "message": str(e)
        }, 404


@uc.route('/users', methods=['POST'])
def add_user():
    user_json_dictionary = request.get_json()  # need to import request from Flask
    user_object = User(  # Dao placeholders: id, username, mobile_phone, active
        None,
        user_json_dictionary['username'],
        user_json_dictionary['mobile_phone'],
        None
    )  # constructor for User object
    try:
        # Dictionary representation of the newly added user
        return user_service.add_user(user_object), 201  # 201 created
    except InvalidParameterError as e:
        return {
            "message": str(e)
        }, 400
