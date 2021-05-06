from flask import Flask, render_template, request, redirect, session
import random 

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def show_index():
        randomNum = random.randint(1, 100)
        session['number'] = randomNum
        return render_template('index.html')

@app.route('/result', methods=["post"])
def show_guess():
    session['guess'] = int(request.form['guess'])
    print(session['guess'], session['number'])
    if  session['guess'] == session['number']:
        return render_template('goodGuess.html')
    else:
        return render_template('badGuess.html')

@app.route('/tryAgain', methods=["post"])
def TryAgain():
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)




