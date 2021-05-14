from flask_app.config.mysqlconnection import connectToMySQL

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_by_id(cls, data):
        query = ('SELECT * FROM ninjas WHERE dojo_id = %(dojo_id)s;')
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        return results;
    
    @classmethod
    def add(cls, data):
        query = ' INSERT INTO ninjas (dojo_id, first_name, last_name, age) VALUES (%(dojo_id)s, %(first_name)s, %(last_name)s, %(age)s);'
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
