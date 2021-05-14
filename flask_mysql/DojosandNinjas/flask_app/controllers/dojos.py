from flask import render_template,redirect,request,session,flash
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.dojo import Dojo

@app.route("/dojo")
def index():
    mysql = connectToMySQL('dojos_and_ninjas_schema')
    dojo = mysql.query_db('SELECT * FROM dojos;')
    return render_template("index.html", dojo=dojo)

@app.route("/showNinjas/<int:id>")
def show_ninjas(id): 
    data= {
        "dojo_id":id
    }
    return render_template("show.html", ninjas= Dojo.get_by_id(data))

@app.route("/addNinja")
def add_ninja(): 
    mysql = connectToMySQL('dojos_and_ninjas_schema')
    dojos = mysql.query_db('SELECT * FROM dojos;') 
    print(dojos)
    return render_template("addNinja.html", dojos= dojos)

@app.route("/create_ninja", methods=["POST"])
def add_friend_to_db():
    ninja = Dojo.add(request.form)
    print(ninja)
    return redirect("/addNinja")


