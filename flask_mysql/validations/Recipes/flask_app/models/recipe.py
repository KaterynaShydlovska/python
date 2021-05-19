from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Recipes:
    def __init__(self, data):
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.time = data['time']
        self.user_id = data['time']
        self.created_at = data['user_id']
        self.updated_at = data['updated_at']

    @staticmethod
    def validate_recipe(data):
        is_valid = True 
        if len(data['name']) < 3:
            flash("Name must be at least 5 characters long!")
            is_valid = False
        if len(data['description']) < 3:
            flash("Description must be at least 5 characters long!")
            is_valid = False                    
        if len(data['instructions']) < 3:
            flash("Instructions must be at least 5 characters long!")
            is_valid = False
        return is_valid

    @classmethod
    def create(cls, data):
        query = ' INSERT INTO  recipe (name, description, instructions,  time, user_id) VALUES ( %(name)s, %(description)s, %(instructions)s, %(time)s, %(user_id)s);'
        res = connectToMySQL('recipes').query_db(query, data)
        return res

    @classmethod
    def getAllrecipes(cls, data):
        query = ' SELECT * FROM recipe LEFT JOIN user ON user.id = recipe.user_id WHERE user.id = %(id)s;'
        res = connectToMySQL('recipes').query_db(query, data)
        return res

    @classmethod
    def getOnerecipes(cls, data):
        query = ' SELECT * FROM recipe WHERE id = %(id)s;'
        res = connectToMySQL('recipes').query_db(query, data)
        return res

    @classmethod
    def updateRecipes(cls, data):
        query = 'UPDATE recipe SET name=%(name)s, description=%(description)s, instructions=%(instructions)s, time=%(time)s WHERE id = %(id)s;'
        res = connectToMySQL('recipes').query_db(query, data)
        return res

        

    @classmethod
    def deleteRecipe(cls, data):
        query = 'DELETE FROM recipe WHERE id = %(id)s;'
        connectToMySQL('recipes').query_db(query, data)



        