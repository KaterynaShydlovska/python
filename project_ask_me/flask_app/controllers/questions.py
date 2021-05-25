from flask import render_template,redirect,request,session,flash
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user import UserInfo
from flask_app.models.question import Questions
from flask import flash
from urllib.request import urlopen
import urllib
import re
import string
import json
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
appid = 'VQRJE8-8VJHJP3U95'

@app.route("/question", methods=["POST"])
def ask(): 
    query = request.form['question']
    print(query)
    data = {"appid": appid, "i": query}
    url = 'http://api.wolframalpha.com/v1/spoken?' + urllib.parse.urlencode(data)
    data = urlopen(url)
    tree = data.read().decode('utf-8')
    tree = re.sub('[%s]' % re.escape(string.punctuation), '', tree)
    print(tree)
    return redirect("/main")
