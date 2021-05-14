from flask_app.config.mysqlconnection import connectToMySQL

class Books:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # @classmethod
    # def get_by_id(cls, data):
    #     query = ('SELECT * FROM books WHERE dojo_id = %(dojo_id)s;')
    #     results = connectToMySQL('books_schema').query_db(query, data)
    #     return results;
    
    @classmethod
    def addAuthor(cls, data):
        query = ' INSERT INTO authors (name) VALUES (%(name)s);'
        return connectToMySQL('books_schema').query_db(query, data)
    
    @classmethod
    def addBook(cls, data):
        query = ' INSERT INTO authors (name) VALUES (%(name)s);'
        return connectToMySQL('books_schema').query_db(query, data)