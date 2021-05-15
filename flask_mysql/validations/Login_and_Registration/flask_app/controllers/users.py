from flask import render_template,redirect,request,session,flash
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user import UserInfo
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route("/")
def index(): 
    return render_template("index.html")

@app.route("/addUser", methods =["POST"])
def add(): 
    if not UserInfo.validate_userInfo(request.form):
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


 
    return redirect(f"succsess/{user_id}")

@app.route("/succsess/<int:id>")
def show(id): 
    data={
        "id": id
    }
    user = UserInfo.getOne(data)
    return render_template("success.html", user = user )

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

    return redirect(f"succsessFullyLogedIn/{session['user_id']}")

@app.route("/succsessFullyLogedIn/<int:id>")
def LogedIn(id): 
    data={
        "id": id
    }
    user = UserInfo.getOne(data)
    return render_template("succsessFullyLogedIn.html", user = user )

@app.route("/logout")
def logout(): 
    session.clear() 
    return redirect("/")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


