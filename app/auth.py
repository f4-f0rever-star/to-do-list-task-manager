import re
import os
import getpass
from app.user import User


USER_FILE = "users.txt"

class Auth:
    USERNAME_PATTERN = r"^[a-zA-Z0-9_]{3,15}$"

    @staticmethod
    def validate_input(username, password):
        if not re.match(Auth.USERNAME_PATTERN, username):
            print("Invalid Username!")
            return False

        if len(password) < 6:
            print("Password too short! Must be at least 6 characters.")
            return False
        return True

    @staticmethod
    def load_users():
        users = []
        if not os.path.exists(USER_FILE):
            return users

        try:            
            with open(USER_FILE, "r") as f:
                for line in f:
                    line = line.strip()
                    if "|" in line:
                        username, password = line.split("|")
                        users.append(User(username, password))
        except Exception as e:
            print(f"Error loading users: {e}")
        return users

   
    @classmethod
    def save_user(cls, user):
        try:
            with open(USER_FILE, "a") as f:
                f.write(f"{user.username}|{user.password}\n")
        except Exception as e:
            print("Unable to save user: {e}")


    @classmethod
    def register(cls):
        print("\n--- User Registration ---")
        username = input("Enter username: ")
        password = getpass.getpass("Enter password: ")
        c_password = getpass.getpass("Confirm password: ")

        if password != c_password:
            print("Password does not match")
            return None

        if not cls.validate_input(username, password):
            return None

        users = cls.load_users()

        if any(user.username == username for user in users):
            print(f"Error: Username '{username}' already exists!")
            return None


        new_user = User(username, password)
        cls.save_user(new_user)
        print("Registration Successful. Welcome!")
        return new_user

   
    @classmethod
    def login(cls):
        print("\n--- Login ---")
        username = input("Username: ")
        password = getpass.getpass("Password: ")

        users = cls.load_users()

        for user in users:
            if user.username.strip() == username.strip() and user.check_password(password):
                print(f"Welcome back, {username}!")
                return user

        print("Invalid username or password!")
        return None
