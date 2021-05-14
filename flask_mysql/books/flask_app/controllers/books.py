from flask import render_template,redirect,request,session,flash
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.book import Books
from flask_app.models.author import Authors


@app.route("/addBook")
def add_book(): 
    mysql = connectToMySQL('books_schema')
    books = mysql.query_db('SELECT * FROM books;') 
    print(books)
    return render_template("books.html", books= books)

@app.route("/saveBook", methods=["POST"])
def add_and_save():
    Books.addBook(request.form)
    return redirect("/addBook")



@app.route("/show/<int:id>")
def showFavorites(id):
    mysql = connectToMySQL('books_schema')
    books = mysql.query_db('SELECT * FROM books;') 
    data= {
        "id":id
    }
    favorites = Books.getFavorite_Books(data)
    print(favorites)
    print("favorites!!!!!!!!!!!!!!!!!!!")
    return render_template("show.html", books= books, favorites = favorites)


