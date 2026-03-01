import json
import hashlib
import re
import os
import getpass
from user import User, Admin

USER_FILE = "users.json"

class Auth:
    USERNAME_PATTERN = r"^[a-zA-Z0-9_]{3,15}$"

    @staticmethod
    def validate_input(username, password):
        if not re.match(Auth.USERNAME_PATTERN, username):
            print("Invalid Username!")
            return False
        return True

    @staticmethod
    def load_users():
         if not os.path.exists(USER_FILE) or os.path.getsize(USER_FILE) == 0:
            return[]
         
         try:            
             with open(USER_FILE, "r") as f:
                data = json.load(f)
                return [User(u["username"], u["password"], u["role"], is_hashed = True) for u in data]
         except (json.JSONDecodeError, KeyError):
            return []

    @classmethod
    def register(cls):
        print("\n--- User Registration ---")
        username = input("Enter username: ")
        password = getpass.getpass("Enter password: ")

        if not cls.validate_input(username, password):
            return None

        users = cls.load_users()
        
        if any(u.username == username for u in users):
            print(f"Error: Username '{username}' already exists!")
            return None

        new_user = User(username, password)
        users.append(new_user)
        
        with open(USER_FILE, "w") as f:
             json.dump([u.to_dict() for u in users], f, indent = 4)

        print("Registration Successful. Welcome!")
        return new_user

    @classmethod
    def login(cls):
        print("\n--- Login ---")
        username = input("Username: ")
        password = getpass.getpass("Password: ")
        
        users = cls.load_users()
        for u in users:
            if u.username == username and u.check_password(password):
                print(f"Welcome back, {username}!")
                return u
            print("Invalid username or password!")
        return None
