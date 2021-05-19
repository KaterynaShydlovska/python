from flask import render_template,redirect,request,session,flash
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user import UserInfo
from flask_app.models.recipe import Recipes
from flask import flash
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route("/")
def index(): 
    return render_template("index.html")

@app.route("/addUser", methods =["POST"])
def add(): 
    if not UserInfo.validate_userInfo(request.form):
        return redirect('/')
    
    data ={
        "email" : request.form['email']
    }
    user_in_db = UserInfo.get_by_email(data)
    if user_in_db:
        flash("Please add new email address, this email address already exist")
        return redirect('/')

    pw_hash = bcrypt.generate_password_hash(request.form['password'])

    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password" : pw_hash
    }
    user_id = UserInfo.save(data)
    session['user_id'] = user_id
    flash("You've been succssesfully regirstres")
    return redirect("/recipes")

@app.route("/recipes")
def show(): 
    if "user_id" not in session:
        flash("Please login or registred!")
        return redirect("/show")
    data={
        "id": session['user_id']
    }
    user = UserInfo.getOne(data)
    recipes = Recipes.getAllrecipes(data)
    return render_template("recipes.html", user = user , recipes = recipes)
    

@app.route("/login", methods =["POST"])
def login(): 
    data = { "email" : request.form["email"] }
    user_in_db = UserInfo.get_by_email(data)
    if not user_in_db:
        flash("Invalid Email/Password")
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash("Invalid Email/Password")
        return redirect('/')
    session['user_id'] = user_in_db.id


    return redirect("/recipes")

@app.route("/logout")
def logout(): 
    session.clear() 
    return redirect("/")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")