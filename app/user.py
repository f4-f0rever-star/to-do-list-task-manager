import hashlib

class Person:
    def __init__(self, username):
        self._username = username

    @property
    def username(self):
        return self._username

class User(Person):
    Valid_roles = ["User", "Guest"]

    def __init__(self, username, password, role = "User", is_hashed = False):
        super().__init__(username)

        if not is_hashed:
            self.password = self.hash_password(password)
        else:
            self.password = password

        if role not in User.Valid_roles:
            self.role = "User"
        else:
            self.role = role

    def hash_password(self, password):
        hash_obj = hashlib.sha256(password.encode())
        full_hash = hash_obj.hexdigest()
        return full_hash[:16]
          
    def check_password(self, password):
        return self.hash_password(password) == self.password

    def to_dict(self):
        return {"username": self.username, "password": self.password, "role": self.role}
    
    def __str__(self):
        return f"[{self.role}] {self.username}  | Status: Authenticated"
    
class Admin(User):
    def __init__(self, username, password):
        super().__init__(username, password, role = "Admin")