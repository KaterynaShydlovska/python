from flask import render_template,redirect,request,session,flash
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.book import Books
from flask_app.models.author import Authors

@app.route("/authors")
def index():
    authors = Authors.getAllAuthors()
    return render_template("index.html", authors = authors)


@app.route("/addAuthor", methods=["POST"])
def add_author():
    Authors.addAuthor(request.form)
    return redirect("/authors")

@app.route("/book_show/<int:id>")
def show(id):
    books = Books.getAllBooks()
    data= {
        "id":id
    }
    mysql = connectToMySQL('books_schema')
    query = ('SELECT * FROM books WHERE id = %(id)s;') 
    book = mysql.query_db(query, data)
    author = Authors.getAuthors_by_Book(data)
    authors = Authors.getAllAuthors()
    print(book[0]['title'])
    return render_template("bookShow.html", book=book, books= books, author=author, authors=authors)

@app.route("/addFavorites/<int:id>", methods=["POST"])
def add_favBook(id):
    Authors.addFavoriteBook(request.form)
    return redirect(f"/show/{id}")

@app.route("/addFavoritesAuthor/<int:id>", methods=["POST"])
def add_favBookAuthor(id):
    print(request.form)
    Authors.addFavoriteAut(request.form)
    return redirect(f"/book_show/{id}")

