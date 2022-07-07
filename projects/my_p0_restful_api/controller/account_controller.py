from flask import Blueprint
from service.account_service import AccountService
from exception.customer_not_found import CustomerNotFoundError

ac = Blueprint('todo_controller', __name__)

account_service = AccountService()


# POST /customer/{customer_id}/accounts
@ac.route('/customer/<customer_id>', methods=['POST'])
def create_customer_account(customer_id):
    pass


# GET /customer/{customer_id}/accounts: Get all accounts for customer with id of X (if customer exists)
# GET /customer/{customer_id}/accounts?amountLessThan=1000&amountGreaterThan=300: Get all accounts for
# customer id of X with balances between Y and Z (if customer exists)
@ac.route('/customer/<customer_id>/accounts')
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
@ac.route('/customer/<customer_id>/account/<account_id>')
def get_customer_account_by_id(customer_id, account_id):
    pass


# PUT /customer/{customer_id}/account/{account_id}: Update account with id of Y belonging to customer with id of X
# (if customer and account exist AND if account belongs to customer)
@ac.route('/customer/<customer_id>/account/<account_id>', methods=['PUT'])
def edit_customer_account_by_id(customer_id, account_id):
    pass


# DELETE /customer/{customer_id}/account/{account_id}: Delete account with id of Y belonging to customer with id of X
# (if customer and account exist AND if account belongs to customer)
@ac.route('/customer/<customer_id>/account/<account_id>', methods=['DELETE'])
def delete_customer_account_by_id(customer_id, account_id):
    pass
