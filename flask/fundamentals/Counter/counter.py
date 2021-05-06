from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'


@app.route('/')
def show_index():
    count = countVisits(request.remote_addr, 1)
    return render_template('index.html', counter=count)

@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect('/')

@app.route('/reset', methods = ["post"])
def reset():
    reset = request.form['reset']
    print(request.form)
    session.clear()
    return redirect('/')

@app.route('/add', methods = ["post"])
def addTwo():
    count = countVisits(request.remote_addr, 1)
    return redirect('/')

def countVisits(request, numb):
    if request in session:
        count = session[request]
        session[request]+= numb
    else:
        session[request] = 1
    return session[request]

if __name__ == "__main__":
    app.run(debug=True)
