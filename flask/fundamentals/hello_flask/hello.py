from flask import Flask
app = Flask(__name__)

@app.errorhandler(Exception)
def server_error(err):
    app.logger.exception(err)
    return "Sorry! No response. Try again", 500

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/success')
def success():
    return "success"

@app.route('/dojo')
def dojo():
    return "Dojo"

@app.route('/say/<name>')
def sayHello(name):
    return "Hello, " + name

@app.route('/repeat/<id>/<text>')
def repeat(id, text):
    return (text + " ") * int(id)

if __name__=="__main__":
    app.run(debug=True)

