from model.admin import Admin

class AdminController():
    @classmethod
    def login(cls, username, password):
        admin = Admin()
        return admin.login(username, password)
        