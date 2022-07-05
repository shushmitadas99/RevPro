class Customer:
    def __init__(self, id, first_name, last_name, mobile_phone, email):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.mobile_phone = mobile_phone
        self.email = email
        # we have to refactor some code in user_dao.py file

    def to_dict(self):
        return{
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "mobile_phone": self.mobile_phone,
            "email": self.email
        }