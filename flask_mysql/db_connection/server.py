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
    mysql.query_db(query, data)
    return redirect("/")


            
if __name__ == "__main__":
    app.run(debug=True)

