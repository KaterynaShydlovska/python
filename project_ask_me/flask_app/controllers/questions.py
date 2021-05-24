from flask import render_template,redirect,request,session,flash
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user import UserInfo
from flask_app.models.question import Questions
from flask import flash
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


# @app.route("/send", methods=["POST"])
# def send(): 


#     data ={
#         "message" : request.form['message'],
#         "to_user_id" : request.form['to_user_id'],
#         "from_user": request.form['from_user']
#     }
#     if not Questions.validate_message(data):
#         redirect("/wall")
#     Questions.send(data)
#     return redirect("/wall")

# @app.route("/delete", methods=["POST"])
# def delete(): 
#     data ={
#         "id": request.form['id']
#     }
#     m = Questions.deleteMessage(data)
#     # print(m)
#     # print("=================")
#     return redirect("/wall")

    
