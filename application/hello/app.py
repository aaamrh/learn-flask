cd ..from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello Flask!</h1>'


@app.route('/greet', defaults={"name":"marh"})
@app.route('/greet/<name>')
def greet(name):
    return'<h1>greet %s!</h1>' % name