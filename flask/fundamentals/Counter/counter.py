from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'


@app.route('/')
def show_index():
    count = 0
    if request.remote_addr in session:
        count = session[request.remote_addr]
        session[request.remote_addr]+= 1
    else:
        session[request.remote_addr] = 1
    return render_template('index.html', counter=count)

@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
