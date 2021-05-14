from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Dojos:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @staticmethod
    def validate_dojo(data):
        is_valid = True # we assume this is true
        if len(data['name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
            if len(data['comment']) < 10:
                flash("Comment must be at least 3 characters.")
                is_valid = False
                return is_valid



    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name, location,language, comment) VALUES (%(name)s, %(location)s, %(language)s, %(comment)s);"
        return connectToMySQL('dojo_survey').query_db(query, data)

    @classmethod
    def get(cls, data):
        query = 'SELECT * FROM dojos WHERE id = %(id)s;'
        res = connectToMySQL('dojo_survey').query_db(query, data);
        print(res[0])
        return res[0]
    