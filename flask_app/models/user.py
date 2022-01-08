from flask_app.config.mysqlconnection import connectToMySQL #These ones access the database
from flask_app.models import puzzle, like, solved
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    def __init__(self, data):
        self.id = data["id"]
        self.username = data["username"]
        self.password = data["password"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @staticmethod
    def validate(data):
        is_valid = True
        if len(data["username"]) < 3:
            flash("First name must be at least three characters!")
            is_valid = False
        if len(data["password"]) < 8:
            flash("Password must be at least eight characters!")
            is_valid = False
        if data["password"] != data["confirmation"]:
            flash("Please type the same password in both fields.")
            is_valid = False
        return is_valid


    @classmethod
    def unique_username(cls,data):
        query = "SELECT * FROM users WHERE username = %(username)s"
        username_db = connectToMySQL("picross_schema").query_db(query,data)
        if len(username_db) < 1:
            return True
        else:
            flash("That username is already taken.")
            return False

    @classmethod
    def add_user(cls,data):
        query = "INSERT INTO users (username, password) VALUES (%(username)s, %(password)s)"
        return connectToMySQL("picross_schema").query_db(query,data)

    @classmethod
    def get_user_by_username(cls,data):
        query = "SELECT * FROM users WHERE username = %(username)s"
        users_db = connectToMySQL("picross_schema").query_db(query,data)
        if len(users_db) < 1:
            return False
        user_instance = User(users_db[0])
        return user_instance