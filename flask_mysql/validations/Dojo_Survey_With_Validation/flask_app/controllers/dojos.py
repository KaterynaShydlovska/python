from flask import render_template,redirect,request,session,flash
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.dojo import Dojos

@app.route("/")
def index(): 
    return render_template("index.html")

@app.route("/add", methods =["POST"])
def add(): 
    res = Dojos.save(request.form)
    if not Dojos.validate_dojo(request.form):
        # redirect to the route where the burger form is rendered.
        return redirect('/')
    # else no errors:
    print(res)
    print("---------")
    return redirect(f"result/{res}")



@app.route("/result/<int:id>")
def show(id): 
    data = {
        'id': id
    }
    userInfo= Dojos.get(data)
    return render_template("show.html", userInfo=userInfo)