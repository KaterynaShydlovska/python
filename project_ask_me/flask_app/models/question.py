from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Questions:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['question']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @staticmethod
    def validate_message(data):
        is_valid = True 
        if len(data['message']) < 3:
            flash("Message must be at least 5 characters long!")
            is_valid = False
        return is_valid
