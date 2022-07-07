from flask import Blueprint, request
from model.customer import Customer
from service.customer_service import CustomerService
from exception.invalid_parameter import InvalidParameterError
from exception.customer_not_found import CustomerNotFoundError

cc = Blueprint('customer_controller', __name__)

# Instantiate a UserService object
customer_service = CustomerService()


# Homepage
@cc.route('/')
def welcome():
    return '''
    
    WELCOME TO BANK OF CANADA
    
    Please enter the following HTTP requests to perform specific operations:
    
    (1) POST /customers: Creates a new customer
    (2) GET /customers: Gets all customers
    (3) GET /customer/{customer_id}: Get customer with an id of X (if the customer exists)
    (4) PUT /customer/{customer_id}: Update customer with an id of X (if the customer exists)
    (5) DELETE /customer/{customer_id}: Delete customer with an id of X (if the customer exists)
    (6) POST /customer/{customer_id}/accounts: Create a new account for a customer with id of X (if customer exists)
    (7) GET /customer/{customer_id}/accounts: Get all accounts for customer with id of X (if customer exists)
    (8) GET /customer/{customer_id}/accounts?amountLessThan=1000&amountGreaterThan=300: Get all accounts for customer 
        id of X with balances between Y and Z (if customer exists)
    (9) GET /customer/{customer_id}/account/{account_id}: Get account with id of Y belonging to customer with id of X 
        (if customer and account exist AND if account belongs to customer)
    (10) PUT /customer/{customer_id}/account/{account_id}: Update account with id of Y belonging to customer with id of 
         X (if customer and account exist AND if account belongs to customer)
    (11) DELETE /customer/{customer_id}/account/{account_id}: Delete account with id of Y belonging to customer with id
         of X (if customer and account exist AND if account belongs to customer)
         
    '''


# POST /customers: Create a new customer
@cc.route('/customers', methods=['POST'])
def create_customer():
    customer_json_dictionary = request.get_json()  # need to import request from Flask
    customer_object = Customer(  # Dao placeholders: id, first_name, last_name, mobile_phone, email
        None,  # id
        customer_json_dictionary['first_name'],
        customer_json_dictionary['last_name'],
        customer_json_dictionary['mobile_phone'],
        customer_json_dictionary['email']
    )  # constructor for Customer object
    try:
        # Dictionary representation of the newly added user
        return customer_service.create_customer(customer_object), 201  # 201 created
    except InvalidParameterError as e:
        return {
            "message": str(e)
        }, 400


# GET /customers: Gets all customers
@cc.route('/customers')
def get_customers():
    return {
        "customers": customer_service.get_customers()
    }


# GET /customer/{customer_id}: Get customer with an id of X (if the customer exists)
@cc.route('/customer/<customer_id>')
def get_customer_by_id(customer_id):
    try:
        return customer_service.get_customer_by_id(customer_id)  # dictionary
    except CustomerNotFoundError as e:
        return {
                   "message": str(e)
               }, 404


# PUT /customer/{customer_id}: Update customer with an id of X (if the customer exists)
@cc.route('/customer/<customer_id>', methods=['PUT'])
def update_customer_by_id(customer_id):
    try:
        json_dictionary = request.get_json()
        return customer_service.update_customer_by_id(
            Customer(
                customer_id,
                json_dictionary['first_name'],
                json_dictionary['last_name'],
                json_dictionary['mobile_phone'],
                json_dictionary['email']
            )
        )
    except CustomerNotFoundError as e:
        return {
            "message": str(e)
        }, 404


# DELETE /customer/{customer_id}: Delete customer with an id of X (if the customer exists)
@cc.route('/customer/<customer_id>', methods=['DELETE'])
def delete_customer_by_id(customer_id):
    try:
        customer_service.delete_customer_by_id(customer_id)  # not a return value since we are not returning anything

        return {
            "message": f"Customer with id {customer_id} deleted successfully"
        }
    except CustomerNotFoundError as e:  # Handles the exception that was raised in user_service layer
        return {
            "message": str(e)
        }, 404
