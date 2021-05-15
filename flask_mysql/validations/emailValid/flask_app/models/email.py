from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Emails:
    def __init__(self, data):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @staticmethod
    def validate_email(data):
        is_valid = True # we assume
        if not EMAIL_REGEX.match(data['email']):
            is_valid= False
            flash("Invalid email address!")
        return is_valid

    @classmethod
    def getAll(cls):
        query = 'SELECT * FROM email_address;'
        emails =connectToMySQL('email_schema').query_db(query)
        return emails 

    @classmethod
    def getEmail(cls, data):
        query = 'SELECT * FROM email_address WHERE id = %(id)s;'
        res = connectToMySQL('email_schema').query_db(query, data)
        return res[0]

    @classmethod
    def addEmail(cls, data):
        query = ' INSERT INTO email_address (email) VALUES (%(email)s);'
        return connectToMySQL('email_schema').query_db(query, data)