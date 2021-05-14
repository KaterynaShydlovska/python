from flask_app.config.mysqlconnection import connectToMySQL

class Authors:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def getAllAuthors(cls):
        query = 'SELECT * FROM authors;'
        return connectToMySQL('books_schema').query_db(query)

    @classmethod
    def addAuthor(cls, data):
        query = ' INSERT INTO authors (name) VALUES (%(name)s);'
        return connectToMySQL('books_schema').query_db(query, data)

    @classmethod
    def getAuthors_by_Book(cls, data):
        query = ' SELECT authors.name, favorites.book_id, favorites.author_id, books.title, books.num_of_pages FROM authors JOIN favorites ON authors.id = favorites.author_id JOIN books ON books.id = favorites.book_id WHERE book_id = %(id)s;'
        result = connectToMySQL('books_schema').query_db(query, data)
        return result

    @classmethod
    def addFavoriteBook(cls, data):
        query = ' INSERT INTO favorites (book_id, author_id) VALUES (%(book_id)s, %(author_id)s);'
        result=  connectToMySQL('books_schema').query_db(query, data)
        return result

    @classmethod
    def addFavoriteAut(cls, data):
        query = ' INSERT INTO favorites (book_id, author_id) VALUES (%(book_id)s, %(author_id)s);'
        result=  connectToMySQL('books_schema').query_db(query, data)
        return result