class User: 
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def check_password(self, password_to_check):
        return self.password == password_to_check

    def __repr__(self):
        return f"<User: {self.username}>"