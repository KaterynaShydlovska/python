from flask import render_template,redirect,request,session,flash
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.book import Books


@app.route("/authors")
def index():
    mysql = connectToMySQL('books_schema')
    authors = mysql.query_db('SELECT * FROM authors;')
    return render_template("index.html", authors = authors)

# @app.route("/showNinjas/<int:id>")
# def show_ninjas(id): 
#     data= {
#         "dojo_id":id
#     }
#     return render_template("show.html", ninjas= Dojo.get_by_id(data))



@app.route("/addAuthor", methods=["POST"])
def add_author():
    Books.addAuthor(request.form)
    return redirect("/authors")

@app.route("/addBook")
def add_book(): 
    mysql = connectToMySQL('books_schema')
    books = mysql.query_db('SELECT * FROM books;') 
    print(books)
    return render_template("books.html", books= books)

@app.route("/show")
def show():
    mysql = connectToMySQL('books_schema')
    books = mysql.query_db('SELECT * FROM books;') 
    print(books)
    return render_template("show.html", books= books)


