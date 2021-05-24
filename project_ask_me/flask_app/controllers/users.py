from flask import render_template,redirect,request,session,flash
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user import UserInfo
from flask_app.models.question import Questions
from flask import flash
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route("/")
def index(): 
    return render_template("index.html")


@app.route("/home")
def home(): 
    return render_template("login.html")

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
    return redirect("/main")
 

@app.route("/main")
def show(): 
    if "user_id" not in session:
        flash("Please login or register!")
        return redirect("/")
    data={
        "id": session['user_id']
    }
    user = UserInfo.getOne(data)
    allquestions = Questions.getAllmessages(data)
    # length = len(allquestions)
    # print(length)
    return render_template("questions.html", user = user , questions = allquestions)
    

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


    return redirect("/main")

@app.route("/logout")
def logout(): 
    session.clear() 
    return redirect("/")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")