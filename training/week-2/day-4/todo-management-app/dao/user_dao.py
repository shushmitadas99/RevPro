from model.user import User

# Right now, we don't have a database to connect to
# So we will store data inside of a collection - probably a dictionary

users = {
    "sushi88": User("sushi88", "647-829-8877"),  # this is the constructor we're invoking to create
    # 'User' object, which we are then storing as a value in the dictionary
    "bachy21": User("bachy21", "512-826-8877"),
    "jane567": User("jane567", "437-657-8877")
}


# structure the above dict in OOP way using class
class UserDao:
    # CRUD operations
    # Create - Insert a new user into our "database"
    # Read   - Retrieve a user or users from our "database"
    # Update - Update a user in our "database"
    # Delete - Delete a user in our "database"

    def get_user_by_username(self, username):
        return users[username]  # returns an "User" object => gives KeyError as key doesn't exist
        # Handling this error in user.controller.py


    def get_all_users(self):
        user_values = []  # create list
        # iterate through the dict values for each of the key:value pairs
        for value in users.values():  # .values() is an in-built dict method that returns all dict values
            user_values.append(value)

        return user_values  # returns a list of "User" objects

    def add_user(self, user_object):
        users[user_object.username] = user_object  # user will represent a User object
        # use the username as the key for the user dictionary and then tag on
        # that user dictionary entirely to add the value

        return user_object

    def edit_user_by_username(self, username, new_user_info_object):  # new_user_info will be User object
        if username == new_user_info_object.username:  # If we are not updating the username, just replace the rest of the info
            users[username] = new_user_info_object
        else:  # otherwise delete the original key-value pair and create a new key-value pair
            del users[username]
            users[new_user_info_object.username] = new_user_info_object

        return new_user_info_object
