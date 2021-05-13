from flask_app.config.mysqlconnection import connectToMySQL

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def add(cls, data):
        query = ' INSERT INTO user_table (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s);'
        return connectToMySQL('user').query_db(query, data)

    @classmethod
    def get_by_id(cls, data):
        query = ('SELECT * FROM user_table WHERE id = %(id)s;')
        results = connectToMySQL('user').query_db(query, data)
        print(results)
        return cls(results[0])

    @classmethod
    def update(cls, data):
        query = "UPDATE user_table SET first_name = %(first_name)s, last_name = %(last_name)s, email= %(email)s  WHERE id = %(id)s;"
        return connectToMySQL('user').query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM user_table WHERE id=%(id)s;"
        return connectToMySQL('user').query_db(query, data)
    