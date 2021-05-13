from flask import Flask, render_template, request, redirect, session

from mysqlconnection import connectToMySQL
app = Flask(__name__)


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
    mysql = connectToMySQL('user')
    # print(request.form)
    query = ' INSERT INTO user_table (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s);'
    data = {
        'first_name': request.form['fname'],
        'last_name': request.form['lname'],
        'email': request.form['email']
    }
    response = mysql.query_db(query, data)
    return redirect("/show/" + str(response))
    # return redirect("/")

@app.route("/show/<id>")
def show_friend(id):
    mysql = connectToMySQL('user')
    query = ('SELECT * FROM user_table WHERE id = %(id)s;') 
    data= {
        "id":int(id)
    }
    user= mysql.query_db(query, data)
    print(user)
    return render_template("show.html", user= user[0])

@app.route("/update/<id>")
def update_friend(id):
    mysql = connectToMySQL('user')
    query = ('SELECT * FROM user_table WHERE id = %(id)s;') 
    data= {
        "id":int(id)
    }
    user= mysql.query_db(query, data)
    print(user)
    return render_template("edit.html", user= user[0])

@app.route("/edit/<id>", methods=["POST"])
def edit_friend(id):
    mysql = connectToMySQL('user')
    query = "UPDATE user_table SET first_name = %(first_name)s, last_name = %(last_name)s, email= %(email)s  WHERE id = %(id)s;"
    data = {
        'first_name': request.form['fname'],
        'last_name': request.form['lname'],
        'email': request.form['email'],
        'id': int(id)
    }
    response = mysql.query_db(query, data)
    print(response)
    
    return redirect("/show/" + id)

@app.route("/delete/<id>")
def delete_friend(id):
    mysql = connectToMySQL('user')
    query = "DELETE FROM user_table WHERE id=%(id)s;"
    data = {
        "id": int(id)
    }
    response =mysql.query_db(query, data)
    print(response)
    print("_____________")
    return redirect("/")






            
if __name__ == "__main__":
    app.run(debug=True)

