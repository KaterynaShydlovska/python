from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Messages:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['message']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @staticmethod
    def validate_message(data):
        is_valid = True 
        if len(data['message']) < 3:
            flash("Message must be at least 5 characters long!")
            is_valid = False
        return is_valid

    @classmethod
    def send(cls, data):
        query = ' INSERT INTO  messages (message, to_user_id, from_user) VALUES ( %(message)s, %(to_user_id)s,%(from_user)s );'
        res = connectToMySQL('messenger').query_db(query, data)
        return res

    @classmethod
    def getAllmessages(cls, data):
        query = ' SELECT * FROM messages LEFT JOIN user ON user.id = to_user_id WHERE user.id = %(id)s;'
        res = connectToMySQL('messenger').query_db(query, data)

        return res

    @classmethod
    def deleteMessage(cls, data):
        query = 'DELETE FROM messages WHERE id = %(id)s;'
        connectToMySQL('messenger').query_db(query, data)



        