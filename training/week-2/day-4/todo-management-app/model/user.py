class User:
    def __init__(self, username, mobile_phone):
        self.username = username
        self.mobile_phone = mobile_phone
        # we have to refactor some of the code in user_dao.py file

    def to_dict(self):
        return{
            "username": self.username,
            "mobile_phone": self.mobile_phone
        }