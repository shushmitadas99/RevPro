from dao.user_dao import UserDao
from exception.invalid_parameter import InvalidParameterError
from exception.user_not_found import UserNotFoundError

class UserService:

    def __init__(self):
        self.user_dao = UserDao()

    # Method logic:
    # Get a list of User objects from the DAO layer
    # convert the User objects into dicts
    # return a list of dicts that each represent the users
    def get_all_users(self):
        list_of_user_objects = self.user_dao.get_all_users()

        # Method 1, use a for loop and do it manually
        list_of_user_dictionaries = []
        for user_obj in list_of_user_objects:
            list_of_user_dictionaries.append(user_obj.to_dict())

        return list_of_user_dictionaries

        # Method 2, Use map()
        # return list(map(lambda x: x.to_dict(), list_of_user_objects))

    # Method logic:
    # Get Ussr object from DAO and convert into a dictionary
    def get_user_by_id(self, user_id):
        user_obj = self.user_dao.get_user_by_id(user_id)  # user.dao.get_user_bu_id will either give us None or a
        # User object

        if not user_obj:
            raise UserNotFoundError(f"User with id {user_id} was not found")

        return user_obj.to_dict()  # turn it into dictionary

    # If user is deleted successfully, then return None (implicitly)
    # If user does not exist, raise UserNotFound exception
    def delete_user_by_id(self, user_id):
        # Execute this block of code if user_dao.delete_user_by_id returns False (which means that we did not delete
        # any records)
        if not self.user_dao.delete_user_by_id(user_id):
            raise UserNotFoundError(f"User with id {user_id} was not found")
        # self.user_dao.delete_user_by_id(user_id) => returns False (if user does not exist)
        # if not self.user_dao.delete_user_by_id(user_id) => True
        # then raise exception UserNotFoundError

    # 1: Check if username is at least 6 characters
    # 2: Check if username contains spaces (not allowed)
    # Invoke add_user() in DAO, passing in a user_object
    # Return the dictionary representation of the return value from that method
    def add_user(self, user_object):
        if " " in user_object.username:
            raise InvalidParameterError("Username cannot contain spaces")

        if len(user_object.username) < 6:
            raise InvalidParameterError("Username must be at least 6 characters")

        added_user_object = self.user_dao.add_user(user_object)
        return added_user_object.to_dict()

    def update_user_by_id(self, user_object):
        updated_user_object = self.user_dao.update_user_by_id(user_object)

        if updated_user_object is None:
            raise UserNotFoundError(f"User with id {user_object.id} was not found")

        return updated_user_object.to_dict()

    # The basic business logic is done here.
    # However, we have to implement INPUT VALIDATION for project 0

