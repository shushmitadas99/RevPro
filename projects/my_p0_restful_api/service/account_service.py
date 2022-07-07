from dao.account_dao import AccountDao
from dao.customer_dao import CustomerDao
from exception.customer_not_found import CustomerNotFoundError


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
