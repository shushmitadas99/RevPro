from flask import Blueprint, request
from model.account import Account
from service.account_service import AccountService
from service.customer_service import CustomerService
from exception.customer_not_found import CustomerNotFoundError
from exception.account_not_found import AccountNotFoundError
from exception.account_does_not_belong_to_customer import AccountDoesNotBelongToCustomerError
from exception.invalid_parameter import InvalidParameterError

ac = Blueprint('todo_controller', __name__)

account_service = AccountService()
customer_service = CustomerService()


# POST /customer/{customer_id}/accounts
@ac.route('/customers/<customer_id>/accounts', methods=['POST'])
def create_customer_account(customer_id):
    # account_json_dictionary = request.get_json()  # need to import request from Flask
    # customer_object = Account(  # Dao placeholders: id, first_name, last_name, mobile_phone, email
    #     None,  # id
    #     account_json_dictionary['balance'],
    #     account_json_dictionary['customer_id'],
    #     account_json_dictionary['account_type_id']
    # )  # constructor for Account object
    # try:
    #     # Dictionary representation of the newly added user
    #     return customer_service.create_customer(customer_object), 201  # 201 created
    # except InvalidParameterError as e:
    #     return {
    #                "message": str(e)
    #            }, 400

    pass


# GET /customer/{customer_id}/accounts: Get all accounts for customer with id of X (if customer exists)
# GET /customer/{customer_id}/accounts?amountLessThan=1000&amountGreaterThan=300: Get all accounts for
# customer id of X with balances between Y and Z (if customer exists)
@ac.route('/customers/<customer_id>/accounts')
def get_all_accounts_by_customer_id(customer_id):
    try:
        return {
            "accounts": account_service.get_all_accounts_by_customer_id(customer_id)
        }
    except CustomerNotFoundError as e:
        return {
            "message": str(e)
        }, 404


# GET /customer/{customer_id}/account/{account_id}: Get account with id of Y belonging to customer with id of X
# (if customer and account exist AND if account belongs to customer)
@ac.route('/customers/<customer_id>/accounts/<account_id>')
def get_customer_account_by_account_id(customer_id, account_id):
    try:
        return account_service.get_customer_account_by_account_id(customer_id, account_id), 200
    except CustomerNotFoundError as e:
        return {
                   "message": str(e)
               }, 404  # Not found
    except AccountNotFoundError as e:
        return {
                   "message": str(e)
               }, 404
    except AccountDoesNotBelongToCustomerError as e:
        return {
                   "message": str(e)
               }, 403  # Forbidden




# PUT /customer/{customer_id}/account/{account_id}: Update account with id of Y belonging to customer with id of X
# (if customer and account exist AND if account belongs to customer)
@ac.route('/customers/<customer_id>/accounts/<account_id>', methods=['PUT'])
def update_customer_account_by_account_id(customer_id, account_id):
    pass


# DELETE /customer/{customer_id}/account/{account_id}: Delete account with id of Y belonging to customer with id of X
# (if customer and account exist AND if account belongs to customer)
@ac.route('/customers/<customer_id>/accounts/<account_id>', methods=['DELETE'])
def delete_customer_account_by_account_id(customer_id, account_id):
    pass