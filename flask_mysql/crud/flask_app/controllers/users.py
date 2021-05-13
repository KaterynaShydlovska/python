from flask import render_template,redirect,request,session,flash
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user import User

@app.route("/")
def index():
    mysql = connectToMySQL('user')
    users = mysql.query_db('SELECT * FROM user_table;') 
   
    print(users)
    return render_template("index.html", users=users)

@app.route("/add")
def add():
    return render_template("add.html")

@app.route("/create_friend", methods=["POST"])
def add_friend_to_db():
    user = User.add(request.form)
    return redirect("/show/" + str(user))

@app.route("/show/<id>")
def show_friend(id): 
    data= {
        "id":int(id)
    }
    print(User.get_by_id(data))
    return render_template("show.html", user= User.get_by_id(data))

@app.route("/update/<id>")
def update_friend(id):
    data= {
        "id":int(id)
    }
    return render_template("edit.html", user= User.get_by_id(data))

@app.route("/edit/<id>", methods=["POST"])
def edit_friend(id):
    data = {
        'first_name': request.form['fname'],
        'last_name': request.form['lname'],
        'email': request.form['email'],
        'id': int(id)
    }  
    User.update(data)
    return redirect("/show/" + id)

@app.route("/delete/<id>")
def delete_friend(id):
    data = {
        "id": int(id)
    }
    User.delete(data)
    return redirect("/")