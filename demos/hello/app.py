from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello Flask!</h1>'

# @app.route('/greet/', defaults={"name":"Programmer"})
# @app.route('/greet/<name>')
# def greet(name):
#     return '<h1>Hello, %s!</h1>' % name

# @app.route('/greet')
# @app.route('/greet/<name>')
# def greet(name="Marh"):
#     return "Hello $s!" % name

# @app.route('/greet/')
# @app.route('/greet/<name>')
# def greet(name='marh'):
#     return'<h1>Hello %s!</h1>' % name
@app.route('/hello', defaults={"name":"marh"})
@app.route('/hello/<name>')
def hello(name):
    return'<h1>Hello %s!</h1>' % name

@app.route('/greet', defaults={"name":"marh"})
@app.route('/greet/<name>')
def greet(name):
    return'<h1>greet %s!</h1>' % name