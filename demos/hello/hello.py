from flask import Flask, make_response, redirect, url_for
import json
    
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello Flask!!</h1>'


@app.route('/greet', defaults={"name":"marh"})
@app.route('/greet/<name>')
def greet(name):
    return'<h1>greet %s!</h1>' % name

@app.route('/set/<name>')
def set_cookie(name):
    
    # response = make_response('<h2>羞羞哒</h2>')
    response = make_response(redirect(url_for('greet',name='haha')))
    response.mimetype = 'text/plain'
    response.set_cookie('name', name, max_age=10)
    return response