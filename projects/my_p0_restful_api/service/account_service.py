from dao.account_dao import AccountDao
from dao.customer_dao import CustomerDao
from exception.customer_not_found import CustomerNotFoundError
from exception.account_not_found import AccountNotFoundError
from exception.account_does_not_belong_to_customer import AccountDoesNotBelongToCustomerError


class AccountService:

    def __init__(self):
        # In AccountService, we are actually utilizing two DAOs
        self.account_dao = AccountDao()
        self.customer_dao = CustomerDao()

    def get_all_accounts_by_customer_id(self, customer_id):
        # CHeck if user actually exists
        if self.customer_dao.get_customer_by_id(customer_id) is None:
            raise CustomerNotFoundError(f"Customer with id {customer_id} was not found")

        return list(map(lambda b: b.to_dict(), self.account_dao.get_all_accounts_by_customer_id(customer_id)))  # list

    def get_customer_account_by_account_id(self, customer_id, account_id):
        if not self.customer_dao.get_customer_by_id(customer_id):
            raise CustomerNotFoundError(f"Customer with id {customer_id} was not found")
        if not self.account_dao.get_account_by_account_id(account_id):
            raise AccountNotFoundError(f"Account with id {account_id} was not found")
        customer_with_account_id_object = self.account_dao.get_customers_account_by_account_id(customer_id, account_id)
        if customer_with_account_id_object is None:
            raise AccountDoesNotBelongToCustomerError(f"Account {account_id} does not belong to customer with id {customer_id}")

        return customer_with_account_id_object.to_dict()

