from flask import render_template,redirect,request,session,flash
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user import UserInfo
from flask_app.models.recipe import Recipes
from flask import flash
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route("/create", methods=["POST"])
def create(): 
    data ={
        "name" : request.form['name'],
        "description" : request.form['description'],
        "instructions" : request.form['instructions'],
        "time": request.form['time'],
        "user_id": session['user_id']
    }
    if not Recipes.validate_recipe(data):
        return redirect("/createRecipe")
    res = Recipes.create(data)
    print(res)
    return redirect("/recipes")


@app.route("/createRecipe")
def addRecipe(): 
    return render_template("createRecipe.html")

@app.route("/showRecipe/<int:id>")
def showRecipe(id): 
    data = {
        "id": id
        }
    recipe= Recipes.getOnerecipes(data)
    return render_template("showRecipe.html", recipe =recipe)

@app.route("/edit/<int:id>")
def editRecipe(id): 
    data = {
        "id": id
        }
    recipe= Recipes.getOnerecipes(data)[0]
    return render_template("edit.html", recipe =recipe)

@app.route("/update/<int:id>", methods=["POST"])
def updateRecipe(id): 
    data = {
        "id": id,
        "name": request.form['name'],
        "description": request.form['description'],
        "instructions": request.form['instructions'],
        "time": request.form['time']
        }
    if not Recipes.validate_recipe(data):
        return redirect(f"/edit/{data['id']}")

    Recipes.updateRecipes(data)
    return redirect("/recipes")



@app.route("/delete/<int:id>")
def delete(id): 
    data ={
        "id": id
    }
    Recipes.deleteRecipe(data)
    return redirect("/recipes")