from flask_app.config.mysqlconnection import connectToMySQL

class Books:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def addAuthor(cls, data):
        query = ' INSERT INTO authors (name) VALUES (%(name)s);'
        return connectToMySQL('books_schema').query_db(query, data)
    
    @classmethod
    def addBook(cls, data):
        query = ' INSERT INTO authors (name) VALUES (%(name)s);'
        return connectToMySQL('books_schema').query_db(query, data)

    @classmethod
    def getFavorite(cls, data):
        query = ' SELECT authors.name, favorites.book_id, favorites.author_id, books.title, books.num_of_pages FROM authors JOIN favorites ON authors.id = favorites.author_id JOIN books ON books.id = favorites.author_id WHERE author_id = %(id)s;'
        #something wrong with object id????
        result = connectToMySQL('books_schema').query_db(query, data)
        return result[0]

    @classmethod
    def getFavorite_by_Book(cls, data):
        query = ' SELECT authors.name, favorites.book_id, favorites.author_id, books.title, books.num_of_pages FROM authors JOIN favorites ON authors.id = favorites.author_id JOIN books ON books.id = favorites.author_id WHERE book_id = %(id)s;'
        #something wrong with object id???? Can't pass it
        result = connectToMySQL('books_schema').query_db(query, data)
        print(result)
        print("------------------")
        return result[0]
        
            

