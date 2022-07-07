class Account:
    def __init__(self, id, balance, customer_id, account_type_id):
        self.id = id
        self.balance = balance
        self.customer_id = customer_id
        self.account_type_id = account_type_id

    def to_dict(self):
        return{
            "id": self.id,
            "balance": self.balance,
            "customer_id": self.customer_id,
            "account_type_id": self.account_type_id
        }