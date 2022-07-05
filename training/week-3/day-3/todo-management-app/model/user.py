class User:
    def __init__(self, id, username, mobile_phone, active):
        self.id = id
        self.username = username
        self.mobile_phone = mobile_phone
        self.active = active
        # we have to refactor some code in user_dao.py file

    def to_dict(self):
        return{
            "id": self.id,
            "username": self.username,
            "mobile_phone": self.mobile_phone,
            "active": self.active
        }