from flask_app.config.mysqlconnection import connectToMySQL

class Books:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def getAllBooks(cls):
        query = 'SELECT * FROM books;'
        return connectToMySQL('books_schema').query_db(query, )

    @classmethod
    def addBook(cls, data):
        query = ' INSERT INTO books (title, num_of_pages) VALUES (%(title)s, %(num_of_pages)s);'
        return connectToMySQL('books_schema').query_db(query, data)

    @classmethod
    def getFavorite_Books(cls, data):
        query = ' SELECT authors.name, books.id, authors.id, books.title, books.num_of_pages FROM authors LEFT JOIN favorites ON authors.id = favorites.author_id LEFT JOIN books ON books.id = favorites.book_id WHERE authors.id = %(id)s;'
        result = connectToMySQL('books_schema').query_db(query, data)
        return result

    
        
            

