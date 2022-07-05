from dao.customer_dao import CustomerDao
from exception.invalid_parameter import InvalidParameterError
from exception.customer_not_found import CustomerNotFoundError


class CustomerService:

    # CustomerService constructor calling the DAO layer
    def __init__(self):
        self.customer_dao = CustomerDao()

    # Create a new customers
    def create_customer(self, customer_object):
        if " " in customer_object.first_name:
            raise InvalidParameterError("Firstname cannot contain spaces")

        if len(customer_object.first_name) < 3:
            raise InvalidParameterError("Firstname must be at least 6 characters")

        created_customer_object = self.customer_dao.create_customer(customer_object)
        return created_customer_object.to_dict()

    # Get all customers
    def get_customers(self):
        list_of_customer_objects = self.customer_dao.get_customers()

        # Method 1, use a for loop and do it manually
        list_of_customer_dictionaries = []
        for customer_obj in list_of_customer_objects:
            list_of_customer_dictionaries.append(customer_obj.to_dict())

        return list_of_customer_dictionaries

    # Get Ussr object from DAO and convert into a dictionary
    def get_customer_by_id(self, customer_id):
        customer_obj = self.customer_dao.get_customer_by_id(customer_id)  # will either give us None or Customer object

        if not customer_obj:
            raise CustomerNotFoundError(f"Customer with id {customer_id} was not found")

        return customer_obj.to_dict()  # turn it into dictionary

    # If user is deleted successfully, then return None (implicitly)
    # If user does not exist, raise UserNotFound exception
    def delete_customer_by_id(self, customer_id):
        # Execute this block of code if user_dao.delete_user_by_id returns False (which means that we did not delete
        # any records)
        if not self.customer_dao.delete_customer_by_id(customer_id):
            raise CustomerNotFoundError(f"Customer with id {customer_id} was not found")
