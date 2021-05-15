from flask import render_template,redirect,request,session,flash
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.email import Emails




@app.route("/")
def index():
    return render_template("index.html")

@app.route("/addEmail", methods=["POST"])
def add_email():
    if not Emails.validate_email(request.form):
        return redirect('/')
    res = Emails.addEmail(request.form)
    return redirect(f"/show/{res}")

@app.route("/show/<int:id>")
def show(id): 
    data = {
        'id': id
    }
    userInfo= Emails.getEmail(data)
    allEmails = Emails.getAll()    
    return render_template("show.html", userInfo=userInfo, allEmails= allEmails)