from flask import Flask, render_template  # added render_template!
import math


app = Flask(__name__)

@app.route('/')
def regularBoard():
    return render_template('index.html', x = 8, y =8)  

@app.route('/4')
def boardOnFour():
    return render_template('index.html', x = 4, y = 8)

@app.route('/<x>/<y>')
def customBoard(x, y):
    return render_template('index.html', x =  int(x), y = int(y))  

@app.route('/<x>/<y>/<color1>/<color2>')
def customBoardColors(x, y, color1, color2):
    return render_template('index.html', x =  int(x), y = int(y))  


if __name__=="__main__":
    app.run(debug=True)