from flask import Flask, render_template  # added render_template!
import os.path
from os import path

app = Flask(__name__)

@app.route('/play')
def play():
    return render_template('index.html', color= "blue", times =10)  

@app.route('/play/<times>')
def playTimes(times):
    return render_template('index.html', color= "blue", times= int(times))  
    
@app.route('/play/<times>/<color>')
def playTimesColor(times, color):
    return render_template('index.html', color= color, times= int(times))  
    
if __name__=="__main__":
    app.run(debug=True)

